from modeltranslation.translator import register ,TranslationOptions
from .models import AboutModel

@register(AboutModel)
class AboutModelTranslationOptions(TranslationOptions):
    fields = ('title','description')
