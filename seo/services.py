from typing import Optional

from django.db.models import Case, Q, Value, When, SmallIntegerField

from .models.url_based import UrlSeo
from .utils import get_path_from_request
from .settings import SEO_USE_URL_FULL_PATH

__all__ = (
    'get_url_seo',
)


def get_url_seo(request) -> Optional[UrlSeo]:
    path = get_path_from_request(request=request)

    if SEO_USE_URL_FULL_PATH:
        objects = (
            UrlSeo.objects
            .filter(
                Q(url=path) |
                Q(url=request.path) |
                Q(is_default=True)
            )
            .annotate(
                priority=Case(
                    When(url=path, then=Value(1)),  # with GET params
                    When(url=request.path, then=Value(2)),  # without GET params
                    When(is_default=True, then=Value(3)),
                    default=Value(0),
                    output_field=SmallIntegerField()
                )
            )
            .order_by('priority')
        )
    else:
        objects = (
            UrlSeo.objects
            .filter(
                Q(url=path) |
                Q(is_default=True)
            )
            .order_by('is_default')
        )
    return objects.first()
