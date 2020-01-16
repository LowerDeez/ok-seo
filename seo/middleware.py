from django.utils.functional import SimpleLazyObject

from .services import get_url_seo

__all__ = (
    'url_seo_middleware',
)


def url_seo_middleware(get_response):
    """
    Middleware to store a lazy `UrlSeo` instance in the request
    """

    def middleware(request):
        request.seo = SimpleLazyObject(lambda: get_url_seo(request))

        response = get_response(request)

        return response

    return middleware
