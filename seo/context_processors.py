from .services import get_url_seo

__all__ = (
    'seo',
)


def seo(request):
    """
    Context processor to store `UrlSeo` instance in the current context
    """
    return {'seo': get_url_seo(request)}
