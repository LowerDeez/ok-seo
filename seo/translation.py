from modeltranslation.translator import translator, TranslationOptions

from .models.instance_based import ModelInstanceSeo
from .models.view_based import ViewSeo
from .models.url_based import UrlSeo

__all__ = (
    'ModelInstanceSeoTranslationOptions',
    'ViewSeoTranslationOptions',
    'UrlSeoTranslationOptions'
)


class ModelInstanceSeoTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'og_title',
        'keywords',
        'description',
        'og_description',
        'alt',
        'h1',
        'seo_text'
    )


class ViewSeoTranslationOptions(ModelInstanceSeoTranslationOptions):
    pass


class UrlSeoTranslationOptions(ModelInstanceSeoTranslationOptions):
    pass


translator.register(ModelInstanceSeo, ModelInstanceSeoTranslationOptions)
translator.register(ViewSeo, ViewSeoTranslationOptions)
translator.register(UrlSeo, UrlSeoTranslationOptions)
