from django.utils.translation import pgettext_lazy

__all__ = (
    'DEFAULT_IMAGE_EXTENSIONS',
    'DEFAULT_OBJECT_TYPES',
    'DEFAULT_TWITTER_TYPES',
    'INDEX_CHOICES',
    'FOLLOW_CHOICES'
)

DEFAULT_IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png']

DEFAULT_OBJECT_TYPES = (
    ('article', pgettext_lazy('OG types', 'Article')),
    ('website', pgettext_lazy('OG types', 'Website')),
)

DEFAULT_TWITTER_TYPES = (
    ('summary', pgettext_lazy('Twitter card types', 'Summary Card')),
    ('summary_large_image', pgettext_lazy('Twitter card types', 'Summary Card with Large Image')),
    ('player', pgettext_lazy('Twitter card types', 'Player')),
    ('app', pgettext_lazy('Twitter card types', 'App')),
)


INDEX_CHOICES = (
    ('index', pgettext_lazy('Index choices', 'Index')),
    ('noindex', pgettext_lazy('Index choices', 'No index')),

)

FOLLOW_CHOICES = (
    ('follow', pgettext_lazy('Follow choices', 'Follow')),
    ('nofollow', pgettext_lazy('Follow choices', 'No follow')),
)
