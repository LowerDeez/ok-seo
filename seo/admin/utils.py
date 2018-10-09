from importlib import import_module

from django.apps import apps
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

__all__ = (
    'get_admin_base_class',
    'get_admin_inline_base_class'
)


def get_admin_base_class():
    """
    Return base admin class
    """
    if apps.is_installed('modeltranslation'):
        return import_module('modeltranslation.admin').TabbedExternalJqueryTranslationAdmin
    return admin.ModelAdmin


def get_admin_inline_base_class():
    """
    Return base inline admin class
    """
    if apps.is_installed('modeltranslation'):
        class TabbedTranslationInline(
            import_module('modeltranslation.admin').TranslationGenericStackedInline):
            class Media:
                js = (
                    'modeltranslation/js/force_jquery.js',
                    '//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js',
                    '//cdn.jsdelivr.net/jquery.mb.browser/0.1/jquery.mb.browser.min.js',
                    'modeltranslation/js/tabbed_translation_fields.js',
                )
                css = {
                    'all': ('modeltranslation/css/tabbed_translation_fields.css',),
                }
        return TabbedTranslationInline
    return GenericStackedInline
