from django.conf import settings as django_settings

from .const import (
    DEFAULT_IMAGE_EXTENSIONS,
    DEFAULT_OBJECT_TYPES, DEFAULT_TWITTER_TYPES
)

__all__ = (
    'SEO_DEFAULT_IMAGE',
    'SEO_IMAGE_WIDTH',
    'SEO_IMAGE_HEIGHT',
    'SEO_OBJECT_IMAGE_FIELD',
    'SEO_IMAGE_EXTENSIONS',

    'SEO_MODELS',

    'SEO_VIEWS_CHOICES',

    'SEO_SITE_NAME',

    'SEO_OG_TYPES',

    'SEO_TWITTER_TYPES',

    'SEO_FB_APP_ID',

    'SEO_HTML_ADMIN_WIDGET',

    'SEO_USE_URL_SEO',

    'SEO_DEBUG_MODE',

    'SEO_IMAGE_STORAGE',

    'SEO_URL_SEO_SITEMAP_PRIORITY',
    'SEO_URL_SEO_SITEMAP_CHANGEFREQ',
    'SEO_VIEWS_CONTEXT_NAME'

)

# image settings
SEO_DEFAULT_IMAGE = getattr(django_settings, 'SEO_DEFAULT_IMAGE', '')
SEO_IMAGE_WIDTH = getattr(django_settings, 'SEO_IMAGE_WIDTH', 1200)
SEO_IMAGE_HEIGHT = getattr(django_settings, 'SEO_IMAGE_HEIGHT', 630)
SEO_OBJECT_IMAGE_FIELD = getattr(django_settings, 'SEO_OBJECT_IMAGE_FIELD', 'image')

# allowed image extensions for seo image
SEO_IMAGE_EXTENSIONS = getattr(
    django_settings,
    'SEO_IMAGE_EXTENSIONS',
    DEFAULT_IMAGE_EXTENSIONS
)

SEO_IMAGE_STORAGE = getattr(
    django_settings,
    'SEO_IMAGE_STORAGE',
    django_settings.DEFAULT_FILE_STORAGE
)

# seo models to limit content type choices
SEO_MODELS = getattr(django_settings, 'SEO_MODELS', [])

# choices of views to add seo data
SEO_VIEWS_CHOICES = getattr(django_settings, 'SEO_VIEWS_CHOICES', [])

SEO_SITE_NAME = getattr(django_settings, 'SEO_SITE_NAME', None)

# choices of open graph object types
SEO_OG_TYPES = getattr(
    django_settings,
    'SEO_OG_TYPES',
    DEFAULT_OBJECT_TYPES
)

# choices of twitter card types
SEO_TWITTER_TYPES = getattr(
    django_settings,
    'SEO_TWITTER_TYPES',
    DEFAULT_TWITTER_TYPES
)

# facebook app id
SEO_FB_APP_ID = getattr(django_settings, 'SEO_FB_APP_ID', '')

SEO_HTML_ADMIN_WIDGET = getattr(
    django_settings,
    'SEO_HTML_ADMIN_WIDGET',
    {}
)

SEO_USE_URL_SEO = getattr(django_settings, 'SEO_USE_URL_SEO', False)

SEO_DEBUG_MODE = getattr(django_settings, 'SEO_DEBUG_MODE', True)

SEO_URL_SEO_SITEMAP_PRIORITY = getattr(
    django_settings,
    'SEO_URL_SEO_SITEMAP_PRIORITY',
    1
)

SEO_URL_SEO_SITEMAP_CHANGEFREQ = getattr(
    django_settings,
    'SEO_URL_SEO_SITEMAP_CHANGEFREQ',
    'always'
)

SEO_VIEWS_CONTEXT_NAME = getattr(
    django_settings,
    'SEO_VIEWS_CONTEXT_NAME',
    'seo'
)
