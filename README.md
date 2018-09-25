# django-ok-seo

This app allows you to add meta tags and OpenGraph properties to your HTML responses.

## Installation

Install with pip:

```python
$ pip install django-ok-seo
```

Update INSTALLED_APPS:

```python
INSTALLED_APPS = [
    ...
    'seo',
    'modeltranslation',  # optional
    ...
]
```

Make migrations
```python
$ python manage.py migrate
```

### Available settings

`SEO_VIEWS_CHOICES` - Tuple of tuples. Where the first value is the 
value to use in code and second is is verbose (translated).
For example:
```python
SEO_VIEWS_CHOICES = (
    ('index', 'Index'),
    ('faq', 'Faq'),
)
```

`SEO_MODELS` - List of models names to limit content type choices for 'ModelInstanceSeo'.

`SEO_DEFAULT_IMAGE` - path to default image, which will be used for 'og:image' property.

`SEO_IMAGE_WIDTH` - value of `width` for image. `1200` by default.

`SEO_IMAGE_HEIGHT` - value of `height` for image. `630` by default.

`SEO_IMAGE_EXTENSIONS` - List of allowed image extensions for ImageField in seo model. 

By default:

```python
['jpg', 'jpeg', 'png']
```

`SEO_OG_TYPES` - Tuple of tuples of open graph object types.

By default:

```python
DEFAULT_OBJECT_TYPES = (
    ('website', pgettext_lazy('OG types', 'Website')),
    ('article', pgettext_lazy('OG types', 'Article'))
)
```

`SEO_TWITTER_TYPES` - Tuple of tuples of twitter card types.

By default:

```python
DEFAULT_TWITTER_TYPES = (
    ('summary', pgettext_lazy('Twitter card types', 'Summary Card')),
    ('summary_large_image', pgettext_lazy('Twitter card types', 'Summary Card with Large Image')),
    ('player', pgettext_lazy('Twitter card types', 'Player')),
    ('app', pgettext_lazy('Twitter card types', 'App')),
)
```

TODO:

* etc

### Basic example to use:


```python
# admin.py

from django.contrib import admin

from seo.admin import ModelInstanceSeoInline

from apps.article.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ModelInstanceSeoInline]
```

```python
# views.py

from django.views.generic import DetailView, TemplateView

from seo.mixins.views import ViewSeoMixin, ModelInstanceViewSeoMixin

from apps.article.models import Article


class IndexView(ViewSeoMixin, TemplateView):
    seo_view = 'index'
    template_name = 'index.html'


class IndexViewJinja(ViewSeoMixin, TemplateView):
    seo_view = 'index'
    template_name = 'jinja/index.jinja'


class ArticleDetailView(ModelInstanceViewSeoMixin, DetailView):
    template_name = 'article.html'
    model = Article
    pk_url_kwarg = 'id'


class ArticleDetailViewJinja(ModelInstanceViewSeoMixin, DetailView):
    template_name = 'jinja/article.jinja'
    model = Article
    pk_url_kwarg = 'id'
```

Your templates

### *.html

```html
{% load seo %}
<head>
    <meta charset="UTF-8">
    {% get_seo_data seo %}
</head>
```

### *.jinja

```html
<head>
    <meta charset="UTF-8">
    {{ get_jinja_seo_data(seo, request) }}
</head>
```

### View seo

To add some meta tags to your view, just go to `/admin/seo/viewseo/add/`.