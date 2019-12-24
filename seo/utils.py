from datetime import datetime
from locale import getlocale, locale_alias

from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import to_locale, get_language
from django.utils.translation.trans_real import language_code_prefix_re

from .settings import SEO_USE_URL_FULL_PATH, SEO_MODELS

__all__ = (
    'image_upload_to',
    'admin_change_url',
    'get_path_from_request',
    'get_seo_models_filters',
    'get_locale'
)


def image_upload_to(instance, filename: str) -> str:
    """
    Util to set upload_to path,
    based on model's class name and date of uploading for image field
    """
    tz_now = datetime.now().strftime('%Y/%m/%d')
    return (
        f"{slugify(instance.__class__.__name__)}/"
        f"{tz_now}/{filename}"
    )


def admin_change_url(obj) -> str:
    """
    Return admin change url for given object
    """
    app_label = obj._meta.app_label
    model_name = obj._meta.model.__name__.lower()
    return reverse(f'admin:{app_label}_{model_name}_change', args=(obj.pk,))


def get_path_from_request(request, full_path: bool = SEO_USE_URL_FULL_PATH):
    """
    Return current path from request, excluding language code
    """
    if full_path:
        path = request.get_full_path()
    else:
        path = request.path

    regex_match = language_code_prefix_re.match(path)

    if regex_match:
        lang_code = regex_match.group(1)
        languages = [
            language_tuple[0] for
            language_tuple in settings.LANGUAGES
        ]
        if lang_code in languages:
            path = path[1 + len(lang_code):]
            if not path.startswith('/'):
                path = '/' + path

    return path


def get_seo_models_filters():
    """
    Return filters to limit `content_type` QuerySet
    """
    apps = []
    models = []
    for item in SEO_MODELS:
        if item:
            app, model = item.lower().rsplit('.', 1)
            apps.append(app)
            models.append(model)
    return {
        'model__in': models,
        'app_label__in': apps
    }


def get_locale(request):
    """
    Return locale like `en_GB`
    """
    if request and hasattr(request, 'LANGUAGE_CODE'):
        language = request.LANGUAGE_CODE
    else:
        language = get_language()
    code = locale_alias.get(language)
    if code and '.' in code:
        locale_tuple = tuple(code.split('.')[:2])
        try:
            return locale_tuple[0]
        except IndexError:
            pass
    return to_locale(language)
