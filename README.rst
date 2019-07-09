============================
django-ok-seo |PyPI version|
============================

|Build Status| |Code Health| |Coverage| |Requirements Status| |Python Versions| |PyPI downloads| |license|
|Project Status|

This app allows you to add meta tags and OpenGraph properties to your HTML responses.

Installation
============

Install with pip:

.. code:: shell

    $ pip install django-ok-seo

Update INSTALLED_APPS:

.. code:: python

    INSTALLED_APPS = [
        ...
        'seo',
        'modeltranslation',  # optional
        'django_jinja',  # optional for jinja2 global function
        ...
    ]

Make migrations

.. code:: shell

    $ python manage.py migrate


If you want to make ``seo models`` translatable, you need to install `django-modeltranslation`_ package. After that run:

.. code:: shell

    $ python manage.py makemigrations
    $ python manage.py migrate

to create new fields in `seo models` for each language.


Features
========

There are two options of usage:

1) ``UrlSeo`` - a model to fetch seo data by an url.

2) ``ViewSeo`` and ``ModelInstanceSeo`` - models to attach seo data for specific views (using choices) and objects (using “generic” relationships). 


Available settings
==================

``SEO_USE_URL_SEO`` - Flag to use (display in an admin interface) only `UrlSeo` model. `False` by default.

``SEO_USE_URL_FULL_PATH`` - Flag to use a whole path, plus an appended query string, to search `UrlSeo` isntances. `False` by default.

``SEO_VIEWS_CHOICES`` - Tuple of tuples for using with `ViewSeo`. The first value is the value to use in s code and a second is a verbose (translated) value.

For example:

.. code:: python

    SEO_VIEWS_CHOICES = (
        ('index', 'Index'),
        ('faq', 'Faq'),
    )


``SEO_MODELS`` - List of models names to limit content type choices for 'ModelInstanceSeo'.

For example (use lowercase):

.. code:: python

    SEO_MODELS = [
        'article.article',
        'auth.user'
    ]


``SEO_DEFAULT_IMAGE`` - Path to default image, which will be used for 'og:image' property.

``SEO_IMAGE_WIDTH`` - Value of `width` for image. `1200` by default.

``SEO_IMAGE_HEIGHT`` - Value of `height` for image. `630` by default.

``SEO_IMAGE_EXTENSIONS`` - List of allowed image extensions for ImageField in seo model. 

``SEO_IMAGE_STORAGE`` - Custom file storage for ImageField in seo model. '`django.core.files.storage.FileSystemStorage`' by default.

``SEO_OBJECT_IMAGE_FIELD`` - A name of field to get image from an object. '`image`' by default.

By default:

.. code:: python
    
    ['jpg', 'jpeg', 'png']


``SEO_OG_TYPES`` - Tuple of tuples of open graph object types.

By default:

.. code:: python

    DEFAULT_OBJECT_TYPES = (
        ('website', pgettext_lazy('OG types', 'Website')),
        ('article', pgettext_lazy('OG types', 'Article'))
    )


``SEO_TWITTER_TYPES`` - Tuple of tuples of twitter card types.

By default:

.. code:: python

    DEFAULT_TWITTER_TYPES = (
        ('summary', pgettext_lazy('Twitter card types', 'Summary Card')),
        ('summary_large_image', pgettext_lazy('Twitter card types', 'Summary Card with Large Image')),
        ('player', pgettext_lazy('Twitter card types', 'Player')),
        ('app', pgettext_lazy('Twitter card types', 'App')),
    )

``SEO_FB_APP_ID`` - Common Facebook application id. Also, You can set custom id in facebook_app_id field for each seo instance.

``SEO_HTML_ADMIN_WIDGET`` - Dictionary with default widget for `top_text` and `bottom_text` text fields in django admin interface.

``SEO_DEBUG_MODE`` - Sets debug mode. If ``True`` adds `<meta name="robots" content="noindex,nofollow">` to all pages.

``SEO_URL_SEO_SITEMAP_PRIORITY`` - `UrlSeo` sitemap priority. `1` by default.

``SEO_URL_SEO_SITEMAP_CHANGEFREQ`` - `UrlSeo` sitemap changefreq. `always` by default.

For example:

.. code:: python

    SEO_HTML_ADMIN_WIDGET = {
        'widget': 'TinyMCE',
        'widget_path': 'tinymce.widgets'
    }


Basic example to use:
=====================

Admin inline (for `ModelInstanceSeo`):
--------------------------------------

.. code:: python

    # admin.py

    from django.contrib import admin

    from seo.admin import ModelInstanceSeoInline

    from apps.article.models import Article

    @admin.register(Article)
    class ArticleAdmin(admin.ModelAdmin):
        inlines = [ModelInstanceSeoInline]
    

Views (examples for all models):
--------------------------------

.. code:: python

    # views.py

    from django.views.generic import DetailView, TemplateView

    from seo.mixins.views import (
        ViewSeoMixin, 
        ModelInstanceViewSeoMixin, 
        UrlSeoMixin
    )

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


    class IndexUrlSeoView(UrlSeoMixin, TemplateView):
        template_name = 'index.html'


    class ArticleUrlSeoDetailView(UrlSeoMixin, DetailView):
        template_name = 'article.html'
        model = Article
        pk_url_kwarg = 'id'


Context processor (for `UrlSeo`):
---------------------------------

.. code:: python

    # ...
    'seo.context_processors.seo',


Middleware (for `UrlSeo`) to use from `request` variable in tepmlates:
----------------------------------------------------------------------

.. code:: python

    MIDDLEWARE = [
        ...

        # seo
        'seo.middleware.url_seo_middleware'
    ]


In templates:


.. code:: html

    {% load seo %}
    <head>
        <meta charset="UTF-8">
        {% get_seo_data request.seo %}
    </head>


Your templates:
===============

\*.html
-------

.. code:: html

    {% load seo %}
    <head>
        <meta charset="UTF-8">
        {% get_seo_data seo %}
    </head>

    <!-- Optional: -->
    ...
    <h1>{{ seo.h1 }}</h1>
    ...
    <div id='seo_text'>
        {{ seo.seo_text|safe }}
    </div>


\*.jinja
--------

.. code:: django

    <head>
        <meta charset="UTF-8">
        {{ get_jinja_seo_data(seo) }}
    </head>
    ...
    <!-- Optional: -->
    ...
    <h1>{{ seo.h1 }}</h1>
    ...
    <div id='seo_text'>
        {{ seo.seo_text|safe }}
    </div>


Inheritance
===============

You can inherit your models from `SeoTagsMixin` and override necessary methods to set custom seo data for your objects.

.. code:: python

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
    

And in a template for your DetailView, you can use:

.. code:: html

    <head>
        <meta charset="UTF-8">
        {% get_seo_data object %}
    </head>
    
where object is your default `context_object_name`.

Also, you can use this way with `ModelInstanceViewSeoMixin` to still use `ModelInstanceSeo`, but get some data from a content object. To reach this goal, you need to override next methods:

.. code:: python

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

If you want to get an image from the content object, you may left the image field empty in `ModelInstanceSeo` instance. If your image field has some specific name, you need to define a property with a name `image`.  


Sitemap
=======

.. code:: python

    # sitemaps.py

    from seo.sitemaps import UrlSeoSitemap

    ...

    sitemaps = {
        'pages': UrlSeoSitemap
    }


    # urls.py

    ...
    from django.contrib.sitemaps import views as sitemap_views
    ...

    from somewhere.sitemaps import sitemaps


    urlpatterns = [
        url(r'^sitemap\.xml$', sitemap_views.index, {'sitemaps': sitemaps}, name='sitemap'),
        url(r'^sitemap-(?P<section>\w+)\.xml$', sitemap_views.sitemap, {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap'),
    ]



.. |PyPI version| image:: https://badge.fury.io/py/django-ok-seo.svg
   :target: https://badge.fury.io/py/django-ok-seo
.. |Build Status| image:: https://travis-ci.org/LowerDeez/ok-seo.svg?branch=master
   :target: https://travis-ci.org/LowerDeez/ok-seo
   :alt: Build status
.. |Code Health| image:: https://api.codacy.com/project/badge/Grade/e5078569e40d428283d17efa0ebf9d19
   :target: https://www.codacy.com/app/LowerDeez/ok-seo
   :alt: Code health
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/django-ok-seo.svg
   :target: https://pypi.org/project/django-ok-seo/
   :alt: Python versions
.. |license| image:: https://img.shields.io/pypi/l/django-ok-seo.svg
   :alt: Software license
   :target: https://github.com/LowerDeez/ok-seo/blob/master/LICENSE
.. |PyPI downloads| image:: https://img.shields.io/pypi/dm/django-ok-seo.svg
   :alt: PyPI downloads
.. |Requirements Status| image:: https://requires.io/github/LowerDeez/ok-seo/requirements.svg?branch=master
.. |Coverage| image:: https://api.codacy.com/project/badge/Coverage/e5078569e40d428283d17efa0ebf9d19    
   :target: https://www.codacy.com/app/LowerDeez/ok-seo
   :alt: Code coverage
.. |Project Status| image:: https://img.shields.io/pypi/status/django-ok-seo.svg
   :target: https://pypi.org/project/django-ok-seo/  
   :alt: Project Status

.. _django-modeltranslation: https://github.com/deschler/django-modeltranslation
