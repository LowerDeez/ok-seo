from django.contrib.sitemaps import Sitemap
from django.db.models import Q
from django.utils.timezone import now

from .const import MATCH_EXACT
from .models.url_based import UrlSeo
from .settings import (
    SEO_URL_SEO_SITEMAP_PRIORITY,
    SEO_URL_SEO_SITEMAP_CHANGEFREQ
)

__all__ = (
    'UrlSeoSitemap',
)


class UrlSeoSitemap(Sitemap):
    priority = SEO_URL_SEO_SITEMAP_PRIORITY
    changefreq = SEO_URL_SEO_SITEMAP_CHANGEFREQ

    def items(self):
        return list(
            UrlSeo
            .objects
            .filter(
                match_type=MATCH_EXACT
            )
            .exclude(
                Q(index='noindex') |
                Q(follow='nofollow')
            )
            .values_list('url', flat=True)
        )

    def location(self, item):
        return item

    def lastmod(self, item):
        return now()
