from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SeoConfig(AppConfig):
    name = 'seo'
    verbose_name = _('Seo')

    def ready(self):
        from seo.checks import register_checks
        register_checks()
