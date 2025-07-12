

from modeltranslation.translator  import TranslationOptions,register
from .models import NewsModel

@register(NewsModel)
class NewsModelTranslationOptions(TranslationOptions):
    fields = ('title','description')
