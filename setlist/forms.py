from django import forms

from .models import Song, Entry, Detail

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}

class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea}
    
