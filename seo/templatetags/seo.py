from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Model
from django.template import Library
from django.utils.translation import to_locale, get_language

from ..settings import SEO_DEBUG_MODE
from ..mixins.models import SeoTagsMixin

__all__ = (
    'get_seo_data',
)

register = Library()


@register.inclusion_tag('seo/seo.html', takes_context=True)
def get_seo_data(context, seo, obj: Model = None):
    """
    Renders meta data for given obj, that can be
    some instance which inherits SeoTagsMixin mixin
    """
    if isinstance(seo, SeoTagsMixin):
        return seo.as_meta(context.request, debug=SEO_DEBUG_MODE, obj=obj)
    request = context.request
    return {
        'request': request,
        'canonical': request.build_absolute_uri(),
        'og_locale': to_locale(get_language()),
        'site_name': get_current_site(context.request),
    }
