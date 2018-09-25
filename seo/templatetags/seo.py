from django.template import Library

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
    return {}


