from django.contrib.sites.shortcuts import get_current_site
from django.template import Library
from django.utils.translation import to_locale, get_language

from ..mixins.models import SeoTagsMixin

register = Library()


@register.inclusion_tag('seo/seo.html', takes_context=True)
def get_seo_data(context, seo):
    """
    Renders meta data for given obj, that can be
    some instance which inherits SeoTagsMixin mixin
    """
    if isinstance(seo, SeoTagsMixin):
        return seo.as_meta(context.request)
    return {
        'request': context.request,
        'og_locale': to_locale(get_language()),
        'site_name': get_current_site(context.request),
    }
