from django.apps import apps

if apps.is_installed('django_jinja'):
    from .jinja_seo import *

from .seo import *
