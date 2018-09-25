from modeltranslation.translator import translator, TranslationOptions

from .models.instance_based import ModelInstanceSeo
from .models.view_based import ViewSeo

__all__ = (
    'ModelInstanceSeoTranslationOptions',
    'ViewSeoTranslationOptions'
)


class ModelInstanceSeoTranslationOptions(TranslationOptions):
    fields = ('title', 'keywords', 'description', 'alt')


class ViewSeoTranslationOptions(ModelInstanceSeoTranslationOptions):
    pass


translator.register(ModelInstanceSeo, ModelInstanceSeoTranslationOptions)
translator.register(ViewSeo, ViewSeoTranslationOptions)
