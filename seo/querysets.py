from django.contrib.contenttypes.models import ContentType
from django.db.models import QuerySet

from .settings import SEO_MODELS

__all__ = (
    'ModelInstanceSeoQuerySet',
)


class ModelInstanceSeoQuerySet(QuerySet):
    """
    QuerySet to deal with ModelInstanceSeo instances
    """

    def filter_by_instance(self, instance):
        """
        Return objects for given instance
        """
        content_type = ContentType.objects.get_for_model(instance)
        item = f'{content_type.app_label}.{content_type.model}'.lower()
        if item not in [seo_model.lower() for seo_model in SEO_MODELS]:
            return self.none()
        return self.filter(content_type=content_type, object_id=instance.pk).distinct()
