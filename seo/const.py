from django.utils.translation import pgettext_lazy

__all__ = (
    'DEFAULT_IMAGE_EXTENSIONS',
    'DEFAULT_OBJECT_TYPES',
    'DEFAULT_TWITTER_TYPES',
    'INDEX_CHOICES',
    'FOLLOW_CHOICES',
    'MATCH_EXACT',
    'MATCH_PREFIX',
    'MATCH_TYPE_CHOICES'
)

DEFAULT_IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png']

DEFAULT_OBJECT_TYPES = (
    ('article', pgettext_lazy('ok:seo', 'Article')),
    ('website', pgettext_lazy('ok:seo', 'Website')),
)

DEFAULT_TWITTER_TYPES = (
    ('summary', pgettext_lazy('ok:seo', 'Summary Card')),
    ('summary_large_image', pgettext_lazy('ok:seo', 'Summary Card with Large Image')),
    ('player', pgettext_lazy('ok:seo', 'Player')),
    ('app', pgettext_lazy('ok:seo', 'App')),
)


INDEX_CHOICES = (
    ('index', pgettext_lazy('ok:seo', 'Index')),
    ('noindex', pgettext_lazy('ok:seo', 'No index')),

)

FOLLOW_CHOICES = (
    ('follow', pgettext_lazy('ok:seo', 'Follow')),
    ('nofollow', pgettext_lazy('ok:seo', 'No follow')),
)

MATCH_EXACT = 'exact'
MATCH_PREFIX = 'prefix'

MATCH_TYPE_CHOICES = (
    (MATCH_EXACT, pgettext_lazy('ok:seo', 'Exact')),
    (MATCH_PREFIX, pgettext_lazy('ok:seo', 'Prefix')),
)
