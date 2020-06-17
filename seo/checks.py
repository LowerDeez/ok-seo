from django.apps import apps
from django.conf import settings
from django.core.checks import Error, Warning, register
from django.utils.module_loading import import_string

from seo import settings as seo_settings

__all__ = (
    'check_seo_models_settings',
    'check_seo_debug_mode',
    'check_html_admin_widget_path',
    'register_checks'
)


def check_seo_models_settings(app_configs, **kwargs):
    """
    Check correct paths in `SEO_MODELS` setting
    """
    errors = []
    seo_models = seo_settings.SEO_MODELS

    for item in seo_models:
        if item:
            parts = item.split('.')
            if len(parts) != 2:
                errors.append(
                    Error(
                        f'Setting SEO_MODELS must contain models in a format:'
                        f' `app_label.model_name`. Check item: `{item}`',
                        hint=None,
                        obj='SEO_MODELS',
                        id='seo.E001',
                    )
                )
            else:
                app_label, model_name = parts
                try:
                    apps.get_model(
                        app_label=app_label,
                        model_name=model_name
                    )
                except LookupError as e:
                    errors.append(
                        Error(
                            f'Setting SEO_MODELS can not import next model: `{item}`.',
                            hint=None,
                            obj='SEO_MODELS',
                            id='seo.E002',
                        )
                    )

    return errors


def check_seo_debug_mode(app_configs, **kwargs):
    """
    Check values of django's `DEBUG` and `SEO_DEBUG_MODE`
    to make sure the correct behavior of the package in a production mode
    """
    warnings = []
    seo_debug = seo_settings.SEO_DEBUG_MODE
    django_debug = settings.DEBUG

    if django_debug is False and seo_debug is True:
        warnings.append(
            Warning(
                'Check your `SEO_DEBUG_MODE` setting for production mode.',
                hint='Your DEBUG setting is False',
                obj='SEO_DEBUG_MODE',
                id='seo.W001',
            )
        )

    return warnings


def check_html_admin_widget_path(app_configs, **kwargs):
    """
    Check correct widget path in `SEO_HTML_ADMIN_WIDGET` setting
    """
    warnings = []
    seo_html_admin_widget = seo_settings.SEO_HTML_ADMIN_WIDGET
    widget_path = seo_html_admin_widget.get('widget_path')
    widget = seo_html_admin_widget.get('widget')

    if widget_path and widget:
        try:
            custom_widget = import_string(f'{widget_path}.{widget}')
        except ImportError as e:
            warnings.append(
                Warning(
                    f'Check your `SEO_HTML_ADMIN_WIDGET` setting: {e}.',
                    hint='Your SEO_HTML_ADMIN_WIDGET setting is incorrect',
                    obj='SEO_HTML_ADMIN_WIDGET',
                    id='seo.W002',
                )
            )

    return warnings


def register_checks():
    for check in [
        check_seo_models_settings,
        check_seo_debug_mode,
        check_html_admin_widget_path
    ]:
        register(check)
