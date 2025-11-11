# Appregistro/models.py
from django.db import models
from django.contrib.auth.models import User

class Vehiculo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vehiculos")
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=20)

    class Meta:
        unique_together = ('usuario', 'placa')  # 🔑 única por usuario

    def __str__(self):
        return f"{self.placa} - {self.marca} ({self.tipo})"
