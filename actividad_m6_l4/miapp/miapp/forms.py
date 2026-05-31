from .models import Usuario
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, min_length=10)

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario           # modelo base
        fields = ['username', 'email', 'edad', 'ciudad']
        widgets = {               # personalizar inputs
            'username': forms.TextInput(
                attrs={'placeholder': 'Tu nombre de usuario'}
            ),
            'ciudad': forms.TextInput(
                attrs={'placeholder': 'Santiago, Valparaíso...'}
            ),
        }