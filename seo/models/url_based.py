from urllib.parse import urlparse

from django.db import models
from django.utils.translation import pgettext_lazy

from .base import BaseSeoModel
from ..mixins.models import SeoTagsMixin
from .. import settings

SEO_VIEWS_CHOICES = settings.SEO_VIEWS_CHOICES

__all__ = (
    'UrlSeo',
)


class UrlSeo(SeoTagsMixin, BaseSeoModel):
    """
    Seo model to add seo staff by a url

    Attrs:
        url (CharField): url
    """

    url = models.CharField(
        pgettext_lazy("Url seo model", "Url"),
        max_length=255,
        unique=True,
        db_index=True
    )
    is_default = models.BooleanField(
        pgettext_lazy("Url seo model", "Is default"),
        default=False,
        help_text=pgettext_lazy(
            "Url seo model",
            "Default instance for all pages."
        ),
    )
    path = property(lambda self: urlparse(self.url).path)

    class Meta:
        verbose_name = pgettext_lazy("Url seo model", "Url seo")
        verbose_name_plural = pgettext_lazy("Url seo model", "Url seo")

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if self.is_default:
            (
                self.__class__.objects
                .filter(is_default=True)
                .update(is_default=False)
            )
        return super().save(*args, **kwargs)
