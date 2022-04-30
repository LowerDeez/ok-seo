from typing import Any, Dict, Optional, TYPE_CHECKING

from django import urls
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Model
from django.template import Library
from django.utils.translation import to_locale, get_language

from ..settings import SEO_DEBUG_MODE
from ..utils import get_i18n_context
from ..mixins.models import SeoTagsMixin

if TYPE_CHECKING:
    from seo.models.base import BaseSeoModel

__all__ = (
    'get_seo_data',
    'translate_url'
)

register = Library()


@register.inclusion_tag('seo/seo.html', takes_context=True)
def get_seo_data(
        context: Dict[str, Any],
        seo: 'BaseSeoModel',
        obj: Model = None
) -> Dict[str, str]:
    """
    Renders meta data for given obj, that can be
    some instance which inherits SeoTagsMixin mixin
    """
    if isinstance(seo, SeoTagsMixin):
        template_context = seo.as_meta(
            request=context.request,
            debug=SEO_DEBUG_MODE,
            obj=obj
        )
    else:
        request = context.request
        template_context = {
            'request': request,
            'canonical': request.build_absolute_uri(),
            'og_locale': to_locale(get_language()),
            'site_name': get_current_site(context.request),
        }
    template_context.update(get_i18n_context())
    return template_context


@register.simple_tag(takes_context=True)
def translate_url(
        context: Dict[str, Any], language: Optional[str]
) -> str:
    """
    Get the absolute URL of the current page for the specified language.

    Usage:
        {% translate_url 'en' %}
    """
    url = context['request'].build_absolute_uri()
    return urls.translate_url(url, language)
