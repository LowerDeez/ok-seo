from django.apps import apps
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import to_locale, get_language


if apps.is_installed('django_jinja'):

    from typing import Dict

    from django_jinja import library

    from ..mixins.models import SeoTagsMixin

    __all__ = (
        'jinja_seo',
    )


    @library.global_function
    @library.render_with("seo/jinja/seo.jinja")
    def get_jinja_seo_data(obj, request) -> Dict[str, str]:
        """
        Renders meta data for given obj, that can be
        some instance which inherits SeoTagsMixin mixin
        """
        if isinstance(obj, SeoTagsMixin):
            return obj.as_meta(request)
        return {
            'request': request,
            'og_locale': to_locale(get_language()),
            'site_name': get_current_site(request),
        }
