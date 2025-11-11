from django import forms
from .models import IngresoVehiculo

class IngresoVehiculoForm(forms.ModelForm):
    class Meta:
        model = IngresoVehiculo
        fields = ['vehiculo']  # 👈 solo este campo
