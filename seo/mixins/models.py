import mimetypes
from typing import Dict

from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import to_locale, get_language

from ..const import DEFAULT_OBJECT_TYPES, DEFAULT_TWITTER_TYPES
from ..settings import (
    SEO_DEFAULT_IMAGE,
    SEO_IMAGE_HEIGHT,
    SEO_IMAGE_WIDTH,
    SEO_SITE_NAME,
    SEO_FB_APP_ID
)

__all__ = (
    'SeoTagsMixin',
)


class SeoTagsMixin:
    """
    Mixin for seo tags in the <head> section
    """

    SEO_IMAGE_FIELD = 'image'

    def get_meta_title(self) -> str:
        """
        Return meta title
        """
        if hasattr(self, 'title'):
            return self.title
        return ''

    def get_meta_description(self) -> str:
        """
        Return meta description
        """
        if hasattr(self, 'description'):
            return self.description
        return ''

    def get_meta_keywords(self) -> str:
        """
        Return meta keywords
        """
        if hasattr(self, 'keywords'):
            return self.keywords
        return ''

    def get_facebook_app_id(self) -> str:
        """
        Return facebook app id
        """
        return SEO_FB_APP_ID

    def get_meta_image_field(self):
        """
        Return image field instance to get image url
        """
        return getattr(self, self.SEO_IMAGE_FIELD, None)

    def get_meta_image(self) -> str:
        """
        Return url of image
        """
        image_field = self.get_meta_image_field()
        if image_field:
            try:
                return image_field.url
            except Exception:
                return SEO_DEFAULT_IMAGE
        return SEO_DEFAULT_IMAGE

    def get_meta_image_alt(self) -> str:
        """
        Return alternative text for image
        """
        if hasattr(self, 'alt'):
            return self.alt
        return self.get_meta_title()

    def get_opengraph_type(self) -> str:
        """
        Return open graph object type
        """
        if hasattr(self, 'object_type'):
            return self.object_type
        return DEFAULT_OBJECT_TYPES[0][0]

    def get_twitter_type(self) -> str:
        """
        Return open graph object type
        """
        if hasattr(self, 'twitter_type'):
            return self.twitter_type
        return DEFAULT_TWITTER_TYPES[0][0]

    def as_meta(self, request) -> Dict[str, str]:
        """
        Return dict available to render meta tags
        """
        meta = {
            'title': self.get_meta_title(),
            'description': self.get_meta_description(),
            'keywords': self.get_meta_keywords(),

            'facebook_app_id': self.get_facebook_app_id(),
            'og_type': self.get_opengraph_type(),
            'site_name': SEO_SITE_NAME or get_current_site(request),
            'og_locale': to_locale(get_language()),
            'url': request.build_absolute_uri(),

            'twitter_type': self.get_twitter_type(),
        }
        image = self.get_meta_image()
        if image:
            meta.update({
                'image': request.build_absolute_uri(image),
                'alt': self.get_meta_image_alt(),
                'mime_type': mimetypes.guess_type(image)[0] or 'image/jpeg',
                'image_width': SEO_IMAGE_WIDTH,
                'image_height': SEO_IMAGE_HEIGHT,
            })
        return meta
