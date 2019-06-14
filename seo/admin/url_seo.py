from django.contrib import admin
from django.utils.translation import pgettext_lazy

from .base_fields import base_seo_fields
from .utils import get_admin_base_class
from .mixins import AdminRichTextFieldMixin
from ..models.url_based import UrlSeo

__all__ = (
    'UrlSeoAdmin',
)


@admin.register(UrlSeo)
class UrlSeoAdmin(AdminRichTextFieldMixin, get_admin_base_class()):
    """
    Url seo admin interface
    """
    change_form_template = 'admin/seo/url_seo.html'

    list_display = [
        'url',
        'title',
        'index',
        'follow',
        'is_default'
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
            'fields': (
                'url',
                'is_default'
            )
        }),
        (pgettext_lazy('Url seo admin', 'Meta'), {
            'fields': base_seo_fields,
        }),
    )
