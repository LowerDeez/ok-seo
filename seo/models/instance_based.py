from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Model
from django.utils.translation import pgettext_lazy

from .base import BaseSeoModel
from ..querysets import ModelInstanceSeoQuerySet
from ..mixins.models import SeoTagsMixin
from ..utils import get_seo_models_filters

__all__ = (
    'ModelInstanceSeo',
)


class ModelInstanceSeo(SeoTagsMixin, BaseSeoModel):
    """
    Seo model, connected to objects

    Attrs:
        content_type (ForeignKey): content type
        object_id (CharField): object id
        content_object (GenericForeignKey): content object
    """

    # The mandatory fields for generic relation
    content_type = models.ForeignKey(
        ContentType,
        verbose_name=pgettext_lazy("ok:seo", "Content Type"),
        help_text=pgettext_lazy(
            "ok:seo",
            "Please select the type (model) "
            "for the relation, you want to build."
        ),
        limit_choices_to=get_seo_models_filters(),
        on_delete=models.CASCADE
    )
    object_id = models.CharField(
        pgettext_lazy("ok:seo", "Object Primary Key"),
        max_length=255,
        help_text=pgettext_lazy(
            "ok:seo",
            "Please enter the ID of the related object."
        ),
    )
    content_object = GenericForeignKey('content_type', 'object_id')

    objects = ModelInstanceSeoQuerySet.as_manager()

    class Meta:
        verbose_name = pgettext_lazy(
            "ok:seo",
            "Model instance seo"
        )
        verbose_name_plural = pgettext_lazy(
            "ok:seo",
            "Model instance seo"
        )

    def __str__(self) -> str:
        return self.title

    def is_inherits(self):
        """
        Checks that content object inherits SeoTagsMixin
        """
        return isinstance(self.content_object, SeoTagsMixin)

    def get_meta_title(self) -> str:
        """
        Return meta title
        """
        if not self.title and self.is_inherits():
            return getattr(self.content_object, 'get_meta_title')()
        return super().get_meta_title()

    def get_og_title(self) -> str:
        """
        Return OpenGraph title
        """
        if not self.og_title and self.is_inherits():
            return getattr(self.content_object, 'get_og_title')()
        return super().get_og_title()

    def get_meta_description(self) -> str:
        """
        Return meta description
        """
        if not self.description and self.is_inherits():
            return getattr(self.content_object, 'get_meta_description')()
        return super().get_meta_description()

    def get_og_description(self) -> str:
        """
        Return OpenGraph description
        """
        if not self.description and self.is_inherits():
            return getattr(self.content_object, 'get_og_description')()
        return super().get_og_description()

    def get_h1_title(self) -> str:
        """
        Return  h1 title
        """
        if not self.h1 and self.is_inherits():
            return getattr(self.content_object, 'get_h1_title')()
        return super().get_h1_title()

    def get_meta_image_field(self, obj: Model = None):
        """
        Return image field instance to get image url
        """
        field = self.image
        if not field:
            if not obj:
                obj = self.content_object
            field = getattr(obj, self.SEO_IMAGE_FIELD, None)
        return field
