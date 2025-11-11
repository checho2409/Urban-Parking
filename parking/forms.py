from django import forms

class ConfiguracionForm(forms.Form):
    nombre = forms.CharField(label='Nombre del sistema', max_length=100)
    email = forms.EmailField(label='Correo de soporte')
from django import forms

class PerfilUsuarioForm(forms.Form):
    nombre = forms.CharField(label='Tu nombre', max_length=100)
    telefono = forms.CharField(label='Teléfono de contacto', max_length=20)

