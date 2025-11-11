from django.db import models

# Create your models here.
from django.db import models
from Apppagos.models import Usuario  # reutilizamos el mismo modelo de usuarios externos
from django.contrib.auth.models import User


class Vehiculo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="vehiculos")
    placa = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo}"


class HistorialIngreso(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name="ingresos")
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Ingreso {self.vehiculo.placa} - {self.fecha_ingreso.strftime('%d/%m/%Y %H:%M')}"
