from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


from about.models import About


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
