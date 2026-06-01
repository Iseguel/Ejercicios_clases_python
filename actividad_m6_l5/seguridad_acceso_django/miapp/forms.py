from django import forms
from .models import Usuario

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario           # modelo base
        fields = ['username', 'email', 'edad', 'ciudad']
        widgets = {               # personalizar inputs
            'username': forms.TextInput(
                attrs={'placeholder': 'Tu nombre de usuario'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'email@ejemplo.com'}
            ),
            'edad': forms.NumberInput(
                attrs={'placeholder': 'Tu edad'}
            ),  
            'ciudad': forms.TextInput(
                attrs={'placeholder': 'Santiago, Valparaíso...'}
            ),
        }