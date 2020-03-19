import mimetypes
from typing import Dict

from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Model
from django.utils.translation import to_locale, get_language

from ..const import DEFAULT_OBJECT_TYPES, DEFAULT_TWITTER_TYPES
from ..settings import (
    SEO_DEFAULT_IMAGE,
    SEO_IMAGE_HEIGHT,
    SEO_IMAGE_WIDTH,
    SEO_OBJECT_IMAGE_FIELD,
    SEO_SITE_NAME,
    SEO_FB_APP_ID
)
from ..utils import get_locale

__all__ = (
    'SeoTagsMixin',
)


class SeoTagsMixin:
    """
    Mixin for seo tags in the <head> section
    """

    SEO_IMAGE_FIELD = SEO_OBJECT_IMAGE_FIELD

    def get_robots_content(self) -> str:
        """
        Return robots content
        """
        index = getattr(self, 'index', None)
        follow = getattr(self, 'follow', None)
        if index and follow:
            return f'{index}, {follow}'
        return ''

    def get_canonical(self, request) -> str:
        """
        Return canonical URL
        """
        canonical = getattr(self, 'canonical', None)
        if canonical and str(canonical).startswith('/'):
            return request.build_absolute_uri(canonical)
        return canonical

    def get_meta_title(self) -> str:
        """
        Return meta title
        """
        return getattr(self, 'title', '')

    def get_og_title(self) -> str:
        """
        Return OpenGraph title
        """
        return getattr(self, 'og_title', None) or self.get_meta_title()

    def get_meta_description(self) -> str:
        """
        Return meta description
        """
        return getattr(self, 'description', '')

    def get_og_description(self) -> str:
        """
        Return OpenGraph description
        """
        return (
            getattr(self, 'og_description', None) or
            self.get_meta_description()
        )

    def get_meta_keywords(self) -> str:
        """
        Return meta keywords
        """
        return getattr(self, 'keywords', '')

    @staticmethod
    def get_facebook_app_id() -> str:
        """
        Return facebook app id
        """
        return SEO_FB_APP_ID

    def get_meta_image_field(self, obj: Model = None):
        """
        Return image field instance to get image url
        """
        return getattr(self, self.SEO_IMAGE_FIELD, None)

    def get_meta_image(self, obj: Model = None) -> str:
        """
        Return url of image
        """
        image_field = self.get_meta_image_field(obj)
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
        return getattr(self, 'alt', self.get_meta_title())

    def get_image_width(self) -> int:
        """
        Return width value for image
        """
        return getattr(self, 'width', SEO_IMAGE_WIDTH)

    def get_image_height(self) -> int:
        """
        Return height value for image
        """
        return getattr(self, 'height', SEO_IMAGE_HEIGHT)

    def get_opengraph_type(self) -> str:
        """
        Return open graph object type
        """
        return getattr(self, 'object_type', DEFAULT_OBJECT_TYPES[0][0])

    def get_twitter_type(self) -> str:
        """
        Return open graph object type
        """
        if hasattr(self, 'twitter_type'):
            return self.twitter_type
        return getattr(self, 'twitter_type', DEFAULT_TWITTER_TYPES[0][0])

    def get_h1_title(self) -> str:
        """
        Return  h1 title
        """
        return getattr(self, 'h1', '')

    def get_seo_text(self) -> str:
        """
        Return  top text
        """
        return getattr(self, 'seo_text', '')

    def as_meta(
            self, request, debug: bool, obj: Model = None
    ) -> Dict[str, str]:
        """
        Return dict available to render meta tags
        """
        meta = {
            'robots': self.get_robots_content(),
            'canonical': (
                self.get_canonical(request) or
                request.build_absolute_uri(request.path)
            ),
            'title': self.get_meta_title(),
            'og_title': self.get_og_title(),
            'description': self.get_meta_description(),
            'og_description': self.get_og_description(),
            'keywords': self.get_meta_keywords(),

            'facebook_app_id': self.get_facebook_app_id(),
            'og_type': self.get_opengraph_type(),
            'site_name': SEO_SITE_NAME or get_current_site(request),
            'og_locale': get_locale(request),

            'twitter_type': self.get_twitter_type(),
            'request': request,
            'debug': debug
        }
        image = self.get_meta_image(obj)
        if image:
            meta.update({
                'image': request.build_absolute_uri(image),
                'alt': self.get_meta_image_alt(),
                'mime_type': mimetypes.guess_type(image)[0] or 'image/jpeg',
                'image_width': self.get_image_width(),
                'image_height': self.get_image_height(),
            })
        return meta
