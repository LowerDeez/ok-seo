from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import pgettext_lazy

from .base_fields import base_seo_fields
from .filters import ContentObjectListFilter, SeoModelsFilter
from .utils import get_admin_base_class
from .mixins import AdminRichTextFieldMixin
from ..models.instance_based import ModelInstanceSeo
from ..utils import admin_change_url

__all__ = (
    'ModelInstanceSeoAdmin',
)


@admin.register(ModelInstanceSeo)
class ModelInstanceSeoAdmin(AdminRichTextFieldMixin, get_admin_base_class()):
    """
    Model instance seo admin interface
    """
    fieldsets = (
        (None, {
            'fields': (
                'content_type', 
                'object_id', 
                'content_object_link', 
            )
        }),
        (pgettext_lazy('Model Instance seo admin', 'Meta'), {
            'fields': base_seo_fields,
        }),
    )

    list_display = ['title', 'index', 'follow', 'content_object_link']
    list_editable = ['index', 'follow']
    list_filter = [
        'index',
        'follow',
        'content_type',
        ContentObjectListFilter,
        SeoModelsFilter
    ]
    readonly_fields = ['content_object_link']
    search_fields = ['title', 'description', 'keywords']

    def content_object_link(self, obj):
        if obj.content_object:
            url = admin_change_url(obj.content_object)
            return mark_safe(
                f'<a href="{url}" target="_blank">'
                f'{obj.content_object}'
                f'</a>'
            )
        return '-'
    content_object_link.short_description = pgettext_lazy(
        'Model instance seo admin', 'Content Object')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('content_object')
