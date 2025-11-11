from django import forms
from .models import Usuario, Vehiculo

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'cedula', 'correo', 'celular', 'rol']


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['tipo', 'marca', 'modelo', 'color', 'placa', 'hora_ingreso', 'fecha_ingreso']
