from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..settings import SEO_MODELS

__all__ = (
    'ContentObjectListFilter',
    'SeoModelsFilter',
)


class ContentObjectListFilter(admin.SimpleListFilter):
    title = _('Content object')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'content_object_is_none'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('yes', _('Exists')),
            ('no', _("Doesn't exist")),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == 'yes':
            ids = []
            for obj in queryset.iterator():
                if obj.content_object is None:
                    ids.append(obj.pk)
            return queryset.filter(id__in=ids)

        if self.value() == 'no':
            ids = []
            for obj in queryset.iterator():
                if obj.content_object is not None:
                    ids.append(obj.pk)
            return queryset.filter(id__in=ids)


class SeoModelsFilter(admin.SimpleListFilter):
    title = _('Seo model')
    parameter_name = 'seo_model'

    def lookups(self, request, model_admin):
        seo_models = set(SEO_MODELS)
        return [(model, model.title()) for model in seo_models]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(content_type__model=self.value())