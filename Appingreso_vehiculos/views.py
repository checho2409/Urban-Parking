from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import IngresoVehiculo   # 👈 cambia al nombre exacto de tu modelo
from .forms import IngresoVehiculoForm

def lista_ingresos(request):
    ingresos = IngresoVehiculo.objects.all()
    return render(request, "inveh/lista.html", {"ingresos": ingresos})

def registrar_ingreso(request):
    if request.method == "POST":
        form = IngresoVehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_ingresos")
    else:
        form = IngresoVehiculoForm()
    return render(request, "inveh/registrar_ingreso.html", {"form": form})

def registrar_salida(request, id):
    ingreso = get_object_or_404(IngresoVehiculo, id=id)
    if request.method == "POST":
        ingreso.fecha_salida = timezone.now()
        ingreso.save()
    return redirect("lista_ingresos")
