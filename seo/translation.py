from modeltranslation.translator import register, TranslationOptions
from .models import Keyword, SEOPage
from .models import Keyword, SEOPage

@register(Keyword)
class KeywordTr(TranslationOptions):
    fields = ("name",)

@register(SEOPage)
class SEOPageTr(TranslationOptions):
    fields = ("title", "description")
