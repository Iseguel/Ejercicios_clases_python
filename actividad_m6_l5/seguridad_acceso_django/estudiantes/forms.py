from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegistroEstudianteForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "curso",
            "direccion",
            "beca",
            "password1",
            "password2",
        ]

        labels = {
            "username": "Nombre de usuario",
            "first_name": "Nombre",
            "last_name": "Apellido",
            "email": "Correo electrónico",
            "curso": "Curso",
            "direccion": "Dirección",
            "beca": "Beca",
            "password1": "Contraseña",
            "password2": "Confirmar contraseña",
        }

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese nombre de usuario"
            }),
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese su nombre"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese su apellido"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese su correo electrónico"
            }),
            "curso": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el curso"
            }),
            "direccion": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese su dirección"
            }),
            "beca": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese beca, si corresponde"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Ingrese su contraseña"
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Repita su contraseña"
        })