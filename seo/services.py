from typing import Optional, TYPE_CHECKING

from django.db.models import Case, Q, Value, When, SmallIntegerField

from .const import MATCH_EXACT, MATCH_PREFIX
from .models.url_based import UrlSeo
from .utils import get_path_from_request

if TYPE_CHECKING:
    from django.http import HttpRequest

__all__ = (
    'get_url_seo',
    'get_url_seo_by_match_type'
)


def get_url_seo(request: 'HttpRequest') -> Optional['UrlSeo']:
    """
    Return `UrlSeo` instance filtered by the current path with or without
    an appended query string, if applicable by settings
    """
    path = get_path_from_request(request=request)
    path_without_params = get_path_from_request(request)

    objects = (
        UrlSeo.objects
        .filter(
            Q(url=path) |
            Q(url=path_without_params) |
            Q(is_default=True)
        )
        .annotate(
            priority=Case(
                When(url=path, then=Value(1)),  # with GET params
                When(url=path_without_params, then=Value(2)),  # without GET params
                When(is_default=True, then=Value(3)),
                default=Value(4),
                output_field=SmallIntegerField()
            )
        )
        .order_by('priority')
    )
    return objects.first()


def get_url_seo_by_match_type(request: 'HttpRequest') -> Optional['UrlSeo']:
    """
    Return `UrlSeo` instance filtered by the current path based on the match type.
    """
    path = get_path_from_request(request=request)

    objects = (
        UrlSeo.objects
        .filter(
            # filter exact urls
            (Q(match_type=MATCH_EXACT) & Q(url__iexact=path)) |
            # filter url by prefix match
            Q(match_type=MATCH_PREFIX) |
            # filter default as backup value
            Q(is_default=True)
        )
        .annotate(
            # set priority to order by
            priority=Case(
                # first - exact match
                When(match_type=MATCH_EXACT, url__iexact=path, then=Value(1)),
                # second - prefix match
                When(match_type=MATCH_PREFIX, then=Value(2)),
                # third - default seo
                When(is_default=True, then=Value(3)),
                default=Value(4),
                output_field=SmallIntegerField()
            )
        )
        .order_by('priority')
    )

    for url_seo in objects:
        match_type = url_seo.match_type
        url = url_seo.url.lower()
        path = path.lower()

        # exact value should be first
        if match_type == MATCH_EXACT and url == path:
            return url_seo

        # check prefix match if exact match wasn't found
        elif match_type == MATCH_PREFIX and path.startswith(url):
            return url_seo

    return objects.first()
