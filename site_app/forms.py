from django import forms
from .models import Anime

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['titulo','descricao', 'genero', ]