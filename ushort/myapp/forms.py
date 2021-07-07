from django import forms
from .models import UrlShort

class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlShort
        fields = ['original_url']
        labels = {'original_url':'Enter your URL'}
        widgets = {
            'original_url': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the URL to short.....'})
        }