from django.conf import settings as django_setting

from .const import (
    DEFAULT_IMAGE_EXTENSIONS,
    DEFAULT_OBJECT_TYPES, DEFAULT_TWITTER_TYPES
)

__all__ = (
    'SEO_DEFAULT_IMAGE',
    'SEO_IMAGE_WIDTH',
    'SEO_IMAGE_HEIGHT',
    'SEO_IMAGE_FIELD_NAME',
    'SEO_IMAGE_EXTENSIONS',

    'SEO_MODELS',

    'SEO_VIEWS_CHOICES',

    'SEO_SITE_NAME',

    'SEO_OG_TYPES',

    'SEO_TWITTER_TYPES'

)

# image settings
SEO_DEFAULT_IMAGE = getattr(django_setting, 'SEO_DEFAULT_IMAGE', '')
SEO_IMAGE_WIDTH = getattr(django_setting, 'SEO_IMAGE_WIDTH', 1200)
SEO_IMAGE_HEIGHT = getattr(django_setting, 'SEO_IMAGE_HEIGHT', 630)

# allowed image extensions for seo image
SEO_IMAGE_EXTENSIONS = getattr(django_setting, 'SEO_IMAGE_EXTENSIONS', DEFAULT_IMAGE_EXTENSIONS)

# seo models to limit content type choices
SEO_MODELS = getattr(django_setting, 'SEO_MODELS', [])

# choices of views to add seo data
SEO_VIEWS_CHOICES = getattr(django_setting, 'SEO_VIEWS_CHOICES', [])

SEO_SITE_NAME = getattr(django_setting, 'SEO_SITE_NAME', None)

# choices of open graph object types
SEO_OG_TYPES = getattr(django_setting, 'SEO_OG_TYPES', DEFAULT_OBJECT_TYPES)

# choices of twitter card types
SEO_TWITTER_TYPES = getattr(django_setting, 'SEO_TWITTER_TYPES', DEFAULT_TWITTER_TYPES)

# facebook app id
SEO_FB_APP_ID = getattr(django_setting, 'SEO_FB_APP_ID', '')

SEO_HTML_ADMIN_WIDGET = getattr(django_setting, 'SEO_HTML_ADMIN_WIDGET', {})