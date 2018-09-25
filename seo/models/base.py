from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import pgettext_lazy

from ..const import (
    INDEX_CHOICES,
    FOLLOW_CHOICES
)
from ..settings import (
    SEO_OG_TYPES,
    SEO_TWITTER_TYPES, 
    SEO_IMAGE_EXTENSIONS
)
from ..utils import image_upload_to

__all__ = (
    'BaseSeoModel',
)

SEO_IMAGE_EXTENSIONS = SEO_IMAGE_EXTENSIONS


class BaseSeoModel(models.Model):
    """
    Base Seo model

    Attrs:
        facebook_app_id (CharField): facebook application id
        object_type (CharField): object type
        twitter_type (CharField): twitter type
        index (CharField): robots index value
        follow (CharField): robots follow value
        title (CharField): meta title
        keywords (CharField): meta keywords
        description (CharField): meta description
        image (VersatileImageField): OG image
        alt (CharField): alt text for image
    """
    facebook_app_id = models.CharField(
        pgettext_lazy('Base seo model', 'Facebook app id'),
        max_length=40,
        blank=True
    )
    object_type = models.CharField(
        pgettext_lazy('Base seo model', 'Open graph type'),
        max_length=40,
        blank=True,
        choices=SEO_OG_TYPES,
    )
    twitter_type = models.CharField(
        pgettext_lazy('Base seo model', 'Twitter type'),
        max_length=40,
        blank=True,
        choices=SEO_TWITTER_TYPES,
    )
    index = models.CharField(
        pgettext_lazy('Base seo model', 'Index robots value'),
        max_length=15,
        blank=True,
        choices=INDEX_CHOICES,
    )
    follow = models.CharField(
        pgettext_lazy('Base seo model', 'Follow robots value'),
        max_length=15,
        blank=True,
        choices=FOLLOW_CHOICES,
    )
    title = models.CharField(
        pgettext_lazy("Base seo model", "Seo Title"),
        max_length=255,
        blank=True
    )
    keywords = models.TextField(
        pgettext_lazy("Base seo model", "Meta Keywords"),
        blank=True,
    )
    description = models.TextField(
        pgettext_lazy("Base seo model", "Meta Description"),
        blank=True,
    )
    image = models.ImageField(
        pgettext_lazy("Base seo model", 'Изображение'),
        upload_to=image_upload_to,
        blank=True, null=True,
        validators=[FileExtensionValidator(SEO_IMAGE_EXTENSIONS)]
    )
    alt = models.CharField(
        pgettext_lazy("Base seo model", "Alt"),
        max_length=255,
        blank=True
    )

    class Meta:
        abstract = True

    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.image.delete(save=False)