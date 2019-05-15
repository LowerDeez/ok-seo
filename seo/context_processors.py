from .services import get_url_seo

__all__ = (
    'seo',
)


def seo(request):
    return {'seo': get_url_seo(request)}
