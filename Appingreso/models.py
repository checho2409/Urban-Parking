from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    rol = models.CharField(max_length=50, default="Empleado")

    def __str__(self):
        return self.user.username
