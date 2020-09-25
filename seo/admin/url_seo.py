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
class UrlSeoAdmin(
    AdminRichTextFieldMixin,
    get_admin_base_class()
):
    """
    Url seo admin interface
    """
    change_form_template = 'admin/seo/url_seo.html'

    list_display = [
        'url',
        'title',
        'match_type',
        'index',
        'follow',
        'is_default'
    ]
    list_editable = [
        'match_type',
        'index',
        'follow'
    ]
    list_filter = [
        'match_type',
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
                'match_type',
                'is_default'
            )
        }),
        (pgettext_lazy('ok:seo', 'Meta'), {
            'fields': base_seo_fields,
        }),
    )
