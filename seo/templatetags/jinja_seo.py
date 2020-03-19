from typing import Any, Dict, TYPE_CHECKING

from django import urls
from django.apps import apps
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Model
from django.utils.translation import to_locale, get_language

from ..settings import SEO_DEBUG_MODE
from ..utils import get_i18n_context
from ..mixins.models import SeoTagsMixin

if TYPE_CHECKING:
    from seo.models.base import BaseSeoModel

__all__ = (
    'get_jinja_seo_data',
    'jinja_translate_url'
)


if apps.is_installed('django_jinja'):

    from django_jinja import library
    import jinja2

    @library.global_function
    @library.render_with("seo/jinja/seo.jinja")
    @jinja2.contextfunction
    def get_jinja_seo_data(
            context: Dict[str, Any],
            seo: 'BaseSeoModel',
            obj: Model = None
    ) -> Dict[str, str]:
        """
        Renders meta data for given obj, that can be
        some instance which inherits SeoTagsMixin mixin
        """
        debug = SEO_DEBUG_MODE
        request = context['request']

        if isinstance(seo, SeoTagsMixin):
            template_context = seo.as_meta(
                request=request,
                debug=debug,
                obj=obj
            )
        else:
            template_context = {
                'request': request,
                'canonical': request.build_absolute_uri(),
                'og_locale': to_locale(get_language()),
                'site_name': get_current_site(request),
            }
        template_context.update(get_i18n_context())
        return template_context


    @library.global_function
    @jinja2.contextfunction
    def jinja_translate_url(
            context: Dict[str, Any], language: str
    ) -> str:
        url = context['request'].build_absolute_uri()
        return urls.translate_url(url, language)
