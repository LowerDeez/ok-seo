from urllib.parse import urlparse

from django.db import models
from django.utils.translation import pgettext_lazy

from .base import BaseSeoModel
from ..const import (
    MATCH_EXACT,
    MATCH_TYPE_CHOICES
)
from ..mixins.models import SeoTagsMixin

__all__ = (
    'UrlSeo',
)


class UrlSeo(SeoTagsMixin, BaseSeoModel):
    """
    Seo model to add seo staff by a url

    Attrs:
        url (CharField): url
        is_default (BooleanField): set the instance as default for all urls
    """
    url = models.CharField(
        pgettext_lazy("ok:seo", "Url"),
        max_length=255,
        unique=True,
        db_index=True
    )
    match_type = models.CharField(
        pgettext_lazy('ok:seo', 'Match type'),
        max_length=40,
        blank=True,
        choices=MATCH_TYPE_CHOICES,
        default=MATCH_EXACT
    )
    is_default = models.BooleanField(
        pgettext_lazy("ok:seo", "Is default"),
        default=False,
        help_text=pgettext_lazy(
            "ok:seo",
            "Default instance for all pages."
        ),
    )
    path = property(lambda self: urlparse(self.url).path)

    class Meta:
        verbose_name = pgettext_lazy("ok:seo", "Url seo")
        verbose_name_plural = pgettext_lazy("ok:seo", "Url seo")

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
