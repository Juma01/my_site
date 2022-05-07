from django import forms
from .models import Profession, Entry


class ProfessionForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Запись:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}