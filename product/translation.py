# product/translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import ProductModel, ProductCategory, ProductField

@register(ProductModel)
class ProductModelTranslationOptions(TranslationOptions):
    fields = ('name', 'description')  # Fields you want to translate


@register(ProductField)
class ProductFieldTranslationOptions(TranslationOptions):
    fields = ('key', 'value')