from django.db import models
from django.db.models import Model
from django.utils.translation import pgettext_lazy

from .base import BaseSeoModel
from ..mixins.models import SeoTagsMixin
from ..settings import SEO_VIEWS_CHOICES

__all__ = (
    'ViewSeo',
)


class ViewSeo(SeoTagsMixin, BaseSeoModel):
    """
    Seo model to add seo staff for views

    Attrs:
        view (CharField): custom view name
    """

    view = models.CharField(
        pgettext_lazy("ok:seo", "View"),
        max_length=100,
        choices=SEO_VIEWS_CHOICES,
        unique=True
    )

    class Meta:
        verbose_name = pgettext_lazy("ok:seo", "View seo")
        verbose_name_plural = pgettext_lazy("ok:seo", "View seo")

    def __str__(self) -> str:
        return self.title

    def get_meta_image_field(self, obj: Model = None):
        """
        Return image field instance to get image url
        """
        field = self.image
        if not field and obj:
            field = getattr(obj, self.SEO_IMAGE_FIELD, None)
        return field
