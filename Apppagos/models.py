from django.db import models

class Usuario(models.Model):
    TIPOS = [
        ("interno", "Interno"),
        ("externo", "Externo"),
    ]

    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(blank=True, null=True)  # ✅ solucion: ahora es opcional
    celular = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=10, choices=TIPOS, default="externo")

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.cedula})"


class Pago(models.Model):
    METODOS_PAGO = [
        ("efectivo", "Efectivo"),
        ("nequi", "Nequi"),
        ("daviplata", "Daviplata"),
        ("pse", "PSE"),
        ("tarjeta", "Tarjeta"),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="pagos")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago de {self.valor} por {self.usuario} ({self.metodo_pago})"
