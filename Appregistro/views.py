from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Vehiculo


@login_required
def registro_usuario(request):
    if request.method == "POST":
        tipo = request.POST.get("tipoVehiculo")
        marca = request.POST.get("marcaVehiculo")
        color = request.POST.get("colorVehiculo")
        modelo = request.POST.get("modeloVehiculo")
        placa = request.POST.get("placaVehiculo")

        # 🔑 Si es admin, puede registrar vehículos para cualquier usuario (extra)
        if request.user.is_superuser:
            usuario = request.user  # o podrías extender para elegir el usuario
        else:
            usuario = request.user

        # Validación: que no se repita la placa en el mismo usuario
        if Vehiculo.objects.filter(usuario=usuario, placa=placa).exists():
            messages.error(request, "⚠️ Ya tienes registrado un vehículo con esa placa.")
        else:
            Vehiculo.objects.create(
                usuario=usuario,
                tipo=tipo,
                marca=marca,
                color=color,
                modelo=modelo,
                placa=placa,
            )
            messages.success(request, "✅ Vehículo registrado correctamente")

        return redirect("registro")  # evita reenvío al refrescar

    # 📌 Aquí la lógica combinada:
    if request.user.is_superuser:
        vehiculos = Vehiculo.objects.all()  # Admin ve todos
    else:
        vehiculos = Vehiculo.objects.filter(usuario=request.user)  # Usuario normal ve solo los suyos

    return render(request, "registro/registro.html", {"vehiculos": vehiculos})


@login_required
def eliminar_vehiculo(request, vehiculo_id):
    try:
        if request.user.is_superuser:
            # 👑 Admin puede eliminar cualquier vehículo
            vehiculo = Vehiculo.objects.get(id=vehiculo_id)
        else:
            # 👤 Usuario normal solo los suyos
            vehiculo = Vehiculo.objects.get(id=vehiculo_id, usuario=request.user)

        vehiculo.delete()
        messages.success(request, "🗑️ Vehículo eliminado correctamente")
    except Vehiculo.DoesNotExist:
        messages.error(request, "⚠️ No se encontró el vehículo o no tienes permiso.")
    return redirect("registro")
