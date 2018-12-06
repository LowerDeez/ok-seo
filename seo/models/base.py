from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import pgettext_lazy

from ..const import (
    INDEX_CHOICES,
    FOLLOW_CHOICES,
    DEFAULT_OBJECT_TYPES,
    DEFAULT_TWITTER_TYPES
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


class BaseSeoModel(models.Model):
    """
    Base Seo model

    Attrs:
        object_type (CharField): object type
        twitter_type (CharField): twitter type
        index (CharField): robots index value
        follow (CharField): robots follow value
        title (CharField): meta title
        keywords (CharField): meta keywords
        description (CharField): meta description
        image (VersatileImageField): OG image
        alt (CharField): alt text for image
        h1 (CharField): H1 title for page
        top_text (TextField): text field for top part of the page
        bottom_text (TextField): text field for bottom part of the page
    """
    object_type = models.CharField(
        pgettext_lazy('Base seo model', 'Open graph type'),
        max_length=40,
        blank=True,
        choices=SEO_OG_TYPES,
        default=DEFAULT_OBJECT_TYPES[0][0]
    )
    twitter_type = models.CharField(
        pgettext_lazy('Base seo model', 'Twitter type'),
        max_length=40,
        blank=True,
        choices=SEO_TWITTER_TYPES,
        default=DEFAULT_TWITTER_TYPES[0][0]
    )
    index = models.CharField(
        pgettext_lazy('Base seo model', 'Index robots value'),
        max_length=15,
        blank=True,
        choices=INDEX_CHOICES,
        default=INDEX_CHOICES[0][0]
    )
    follow = models.CharField(
        pgettext_lazy('Base seo model', 'Follow robots value'),
        max_length=15,
        blank=True,
        choices=FOLLOW_CHOICES,
        default=FOLLOW_CHOICES[0][0]
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
    h1 = models.CharField(
        pgettext_lazy("Base seo model", "H1 title"),
        max_length=255,
        blank=True
    )
    top_text = models.TextField(
        pgettext_lazy("Base seo model", "Page top text for seo"),
        blank=True,
        help_text=pgettext_lazy(
            "Base seo model", 
            "Can be usefull for some static pages or some objects (like product category)."
        ),
    )
    bottom_text = models.TextField(
        pgettext_lazy("Base seo model", "Page bottom text for seo"),
        blank=True,
        help_text=pgettext_lazy(
            "Base seo model", 
            "Can be usefull for some static pages or some objects (like product category)."
        ),
    )

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.image.delete(save=False)