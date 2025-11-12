# Apphistorial/views.py
from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import FieldDoesNotExist

# Ajusta la importación de Vehiculo según esté en tu app registro

def historial_view(request):
        return render(request, "historial/historial.html")