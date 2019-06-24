from typing import Dict

from django.apps import apps
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Model
from django.utils.translation import to_locale, get_language

from ..settings import SEO_DEBUG_MODE
from ..mixins.models import SeoTagsMixin

__all__ = (
    'get_jinja_seo_data',
)


if apps.is_installed('django_jinja'):

    from django_jinja import library
    import jinja2

    @library.global_function
    @library.render_with("seo/jinja/seo.jinja")
    @jinja2.contextfunction
    def get_jinja_seo_data(context, seo, obj: Model=None) -> Dict[str, str]:
        """
        Renders meta data for given obj, that can be
        some instance which inherits SeoTagsMixin mixin
        """
        debug = SEO_DEBUG_MODE
        request = context['request']

        if isinstance(seo, SeoTagsMixin):
            return seo.as_meta(request, debug=debug, obj=obj)
        return {
            'request': request,
            'canonical': request.build_absolute_uri(),
            'og_locale': to_locale(get_language()),
            'site_name': get_current_site(request),
        }
