# Appingreso_vehiculos/models.py
from django.db import models
from django.utils import timezone
from Appregistro.models import Vehiculo   # 👈 importamos el modelo de Appregistro

class IngresoVehiculo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name="ingresos")
    fecha_entrada = models.DateTimeField(default=timezone.now)
    fecha_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Ingreso {self.vehiculo.placa} - {self.fecha_entrada.strftime('%d/%m/%Y %H:%M')}"
