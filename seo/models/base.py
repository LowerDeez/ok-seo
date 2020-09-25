from django.core.files.storage import get_storage_class
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
    SEO_IMAGE_EXTENSIONS,
    SEO_IMAGE_WIDTH,
    SEO_IMAGE_HEIGHT,
    SEO_IMAGE_STORAGE
)
from ..utils import image_upload_to

__all__ = (
    'BaseSeoModel',
)


image_storage = get_storage_class(SEO_IMAGE_STORAGE)


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
        pgettext_lazy('ok:seo', 'Open graph type'),
        max_length=40,
        blank=True,
        choices=SEO_OG_TYPES,
        default=DEFAULT_OBJECT_TYPES[0][0]
    )
    twitter_type = models.CharField(
        pgettext_lazy('ok:seo', 'Twitter type'),
        max_length=40,
        blank=True,
        choices=SEO_TWITTER_TYPES,
        default=DEFAULT_TWITTER_TYPES[0][0]
    )
    index = models.CharField(
        pgettext_lazy('ok:seo', 'Index robots value'),
        max_length=15,
        blank=True,
        choices=INDEX_CHOICES,
        default=INDEX_CHOICES[0][0]
    )
    follow = models.CharField(
        pgettext_lazy('ok:seo', 'Follow robots value'),
        max_length=15,
        blank=True,
        choices=FOLLOW_CHOICES,
        default=FOLLOW_CHOICES[0][0]
    )
    canonical = models.CharField(
        pgettext_lazy('ok:seo', 'Canonical'),
        max_length=255,
        blank=True
    )
    title = models.CharField(
        pgettext_lazy('ok:seo', 'Title'),
        max_length=255,
        blank=True
    )
    og_title = models.CharField(
        pgettext_lazy('ok:seo', 'OpenGraph Title'),
        max_length=255,
        blank=True
    )
    keywords = models.TextField(
        pgettext_lazy('ok:seo', 'Keywords'),
        blank=True,
    )
    description = models.TextField(
        pgettext_lazy('ok:seo', 'Description'),
        blank=True,
    )
    og_description = models.TextField(
        pgettext_lazy('ok:seo', 'OpenGraph Description'),
        blank=True,
    )
    image = models.ImageField(
        pgettext_lazy('ok:seo', 'Image'),
        upload_to=image_upload_to,
        blank=True, null=True,
        storage=image_storage(),
        validators=[FileExtensionValidator(SEO_IMAGE_EXTENSIONS)]
    )
    width = models.PositiveIntegerField(
        pgettext_lazy('ok:seo', 'Image width'),
        default=SEO_IMAGE_WIDTH
    )
    height = models.PositiveIntegerField(
        pgettext_lazy('ok:seo', 'Image height'),
        default=SEO_IMAGE_HEIGHT
    )
    alt = models.CharField(
        pgettext_lazy('ok:seo', 'Image alt text'),
        max_length=255,
        blank=True
    )
    h1 = models.CharField(
        pgettext_lazy('ok:seo', 'H1 title'),
        max_length=255,
        blank=True
    )
    seo_text = models.TextField(
        pgettext_lazy('ok:seo', 'Seo text'),
        blank=True,
        help_text=pgettext_lazy(
            'ok:seo',
            'Can be useful for some static pages '
            'or some objects (like product category).'
        ),
    )

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        super().delete(using=using, keep_parents=keep_parents)
        self.image.delete(save=False)
