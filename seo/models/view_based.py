from django.db import models
from django.utils.translation import pgettext_lazy

from .base import BaseSeoModel
from ..mixins.models import SeoTagsMixin
from .. import settings

SEO_VIEWS_CHOICES = settings.SEO_VIEWS_CHOICES

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
        pgettext_lazy("View seo", "View"),
        max_length=100,
        choices=SEO_VIEWS_CHOICES,
        unique=True
    )

    class Meta:
        verbose_name = pgettext_lazy("Model instance seo", "View seo")
        verbose_name_plural = pgettext_lazy("Model instance seo", "View seo")

    def __str__(self) -> str:
        return self.title
