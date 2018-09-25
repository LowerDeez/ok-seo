from django.urls import reverse
from django.utils.timezone import localtime, now
from django.utils.text import slugify

__all__ = (
    'image_upload_to',
    'admin_change_url'
)


def image_upload_to(instance, filename) -> str:
    """
    Util to set upload_to path,
    based on model's class name and date of uploading for image field
    """
    tz_now = localtime(now()).strftime('%Y/%m/%d')
    return f"{slugify(instance.__class__.__name__)}/{tz_now}/{filename}"


def admin_change_url(obj) -> str:
    """
    Return admin change url for given object
    """
    app_label = obj._meta.app_label
    model_name = obj._meta.model.__name__.lower()
    return reverse(f'admin:{app_label}_{model_name}_change', args=(obj.pk,))
