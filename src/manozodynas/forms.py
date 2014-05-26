from django import forms

from models import WordWithoutTranslation

class WordWithoutTranslationForm(forms.ModelForm):
    class Meta:
        model = WordWithoutTranslation

