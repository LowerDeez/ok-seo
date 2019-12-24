from django.apps import apps
from django.conf import settings
from django.core.checks import Error, Warning, register

from seo import settings as seo_settings

__all__ = (
    'check_seo_models_settings',
    'check_seo_debug_mode'
)


def check_seo_models_settings(app_configs, **kwargs):
    errors = []
    seo_models = seo_settings.SEO_MODELS

    for item in seo_models:
        if item:
            parts = item.split('.')
            if len(parts) != 2:
                errors.append(
                    Error(
                        f'Setting SEO_MODELS must contain models in a format:'
                        f' `app_label.model_name`. Check item: `{item}`',
                        hint=None,
                        obj='SEO_MODELS',
                        id='seo.E001',
                    )
                )
            else:
                app_label, model_name = parts
                try:
                    apps.get_model(
                        app_label=app_label,
                        model_name=model_name
                    )
                except LookupError as e:
                    errors.append(
                        Error(
                            f'Setting SEO_MODELS can not import next model: `{item}`.',
                            hint=None,
                            obj='SEO_MODELS',
                            id='seo.E002',
                        )
                    )

    return errors


def check_seo_debug_mode(app_configs, **kwargs):
    warnings = []
    seo_debug = seo_settings.SEO_DEBUG_MODE
    django_debug = settings.DEBUG

    if django_debug is False and seo_debug is True:
        warnings.append(
            Warning(
                'Check your `SEO_DEBUG_MODE` setting for production mode.',
                hint='Your DEBUG setting is False',
                obj='SEO_DEBUG_MODE',
                id='seo.W001',
            )
        )

    return warnings


def register_checks():
    for check in [
        check_seo_models_settings,
        check_seo_debug_mode
    ]:
        register(check)
