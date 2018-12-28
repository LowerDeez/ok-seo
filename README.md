# django-ok-seo

This app allows you to add meta tags and OpenGraph properties to your HTML responses.

## Installation

Install with pip:

```shell
$ pip install django-ok-seo
```

If you want to make seo models translatable, you need to install [django-modeltranslation](https://github.com/deschler/django-modeltranslation) package. After that run:
```shell
$ python manage.py makemigrations
$ python manage.py migrate
```
to create new feelds in seo models for each language.

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
```shell
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
`SEO_FB_APP_ID` - Common Facebook application id. Also, You can set custom id in facebook_app_id field for each seo instance.

`SEO_HTML_ADMIN_WIDGET` -  dictionary with default widget for `top_text` and `bottom_text` text fields in django admin interface.

For example:

```python
SEO_HTML_ADMIN_WIDGET = {
    'widget': 'TinyMCE',
    'widget_path': 'tinymce.widgets'
}
```

TODO:

* etc

### Basic example to use:

Admin inline:

```python
# admin.py

from django.contrib import admin

from seo.admin import ModelInstanceSeoInline

from apps.article.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ModelInstanceSeoInline]
```

Views:
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

Your templates:

### *.html

```html
{% load seo %}
<head>
    <meta charset="UTF-8">
    {% get_seo_data seo %}
</head>

<!-- Optional: -->
...
<h1>{{ seo.h1 }}</h1>
...
<div id='seo_top'>
    {{ seo.top_text|safe }}
</div>
...
<div id='seo_bottom'>
    {{ seo.bottom_text|safe }}
</div>
```

### *.jinja

```django
<head>
    <meta charset="UTF-8">
    {{ get_jinja_seo_data(seo, request) }}
</head>
...
<!-- Optional: -->
...
<h1>{{ seo.h1 }}</h1>
...
<div id='seo_top'>
    {{ seo.top_text|safe }}
</div>
...
<div id='seo_bottom'>
    {{ seo.bottom_text|safe }}
</div>
```

### View seo

To add some meta tags to your view, just go to `/admin/seo/viewseo/add/`.

### Inheritance

You can inherit your models from `SeoTagsMixin` and override necessary methods to set custom seo data for your objects.

```python
from django.db import models

from seo.mixins.models import SeoTagsMixin


class Article(SeoTagsMixin, models.Model):
    preview = models.ImageField()
    short_description = models.TextField(max_length=1000)
    ...

    def get_meta_description(self) -> str:
        """
        Return meta description
        """
        return self.short_description

    def get_meta_image_field(self):
        """
        Return image field instance to get image url
        """
        return self.preview
```
And in a template for your DetailView, you can use:
```html
<head>
    <meta charset="UTF-8">
    {% get_seo_data object %}
</head>
```
where object is your default `context_object_name `.

Also, you can use this way with `ModelInstanceViewSeoMixin` to still use `ModelInstanceSeo`, but get some data from a content object. To reach this goal, you need to override next methods:
```python
def get_meta_title(self) -> str:
    """
    Return meta title
    """
    return _('{} < Some super title').format(str(self))

def get_meta_description(self) -> str:
    """
    Return meta description
    """
    return _(
        '{} ➤ Wow! '
        '✔ Amazing! '
        '❖ Marvelous!'
    ).format(str(self))

def get_h1_title(self) -> str:
    """
    Return  h1 title
    """
    return str(self)
```
> If you want to get image from the content object, you may left the image field empty in a `ModelInstanceSeo` instance. If your image field has some specific name, you need to define a property with a name `image`.  