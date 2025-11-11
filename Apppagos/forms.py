from django import forms
from django.contrib.auth.models import User
from .models import Pago

class PagoForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=User.objects.all(),  # Aquí cargas todos los usuarios externos
        empty_label="Seleccione un usuario",
        widget=forms.Select(attrs={'class': 'pago-select'})
    )

    class Meta:
        model = Pago
        fields = ['usuario', 'monto', 'metodo_pago']
        widgets = {
            'monto': forms.NumberInput(attrs={'class': 'pago-input', 'placeholder': 'Monto a pagar'}),
            'metodo_pago': forms.Select(attrs={'class': 'pago-select'}),
        }
