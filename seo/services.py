from typing import Optional

from django.db.models import Q

from .models.url_based import UrlSeo
from .utils import get_path_from_request

__all__ = (
    'get_url_seo',
)


def get_url_seo(request) -> Optional[UrlSeo]:
    path = get_path_from_request(request=request)
    objects = (
        UrlSeo.objects
        .filter(
            Q(url=path) |
            Q(is_default=True)
        )
        .order_by('is_default')
    )
    return objects.first()
