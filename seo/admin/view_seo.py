from django.contrib import admin
from django.utils.translation import pgettext_lazy

from .base_fields import base_seo_fields
from .utils import get_admin_base_class
from .mixins import AdminRichTextFieldMixin
from ..models.view_based import ViewSeo

__all__ = (
    'ViewSeoAdmin',
)


@admin.register(ViewSeo)
class ViewSeoAdmin(
    AdminRichTextFieldMixin,
    get_admin_base_class()
):
    """
    View seo admin interface
    """
    list_display = [
        'view',
        'title',
        'index',
        'follow'
    ]
    list_editable = [
        'index',
        'follow'
    ]
    list_filter = [
        'index',
        'follow'
    ]
    search_fields = [
        'title',
        'og_title',
        'description',
        'og_description',
        'keywords'
    ]

    fieldsets = (
        (None, {
            'fields': ('view', )
        }),
        (pgettext_lazy('ok:seo', 'Meta'), {
            'fields': base_seo_fields,
        }),
    )
