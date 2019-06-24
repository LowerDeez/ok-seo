from django.utils.translation import pgettext_lazy

from .mixins import AdminRichTextFieldMixin
from .utils import get_admin_inline_base_class
from ..models.instance_based import ModelInstanceSeo

__all__ = (
    'ModelInstanceSeoInline',
)


class ModelInstanceSeoInline(
    AdminRichTextFieldMixin,
    get_admin_inline_base_class()
):
    classes = ['collapse']
    extra = 1
    model = ModelInstanceSeo
    max_num = 1
    verbose_name = pgettext_lazy("Model instance seo admin inline", "Seo")
    verbose_name_plural = pgettext_lazy("Model instance seo admin inline", "Seo")
