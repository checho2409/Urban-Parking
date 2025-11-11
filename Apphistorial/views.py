# Apphistorial/views.py
from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import FieldDoesNotExist

# Ajusta la importación de Vehiculo según esté en tu app registro
from Appregistro.models import Vehiculo


def historial_view(request):
    q = request.GET.get("q", "").strip()

    # Intentamos detectar si Vehiculo tiene un campo FK llamado 'usuario'
    try:
        usuario_field = Vehiculo._meta.get_field('usuario')
    except FieldDoesNotExist:
        usuario_field = None

    # Si existe la FK 'usuario' usaremos el modelo remoto y haremos prefetch
    if usuario_field:
        user_model = usuario_field.remote_field.model
        accessor_name = usuario_field.remote_field.get_accessor_name()  # p.ej. 'vehiculo_set' o 'vehiculos'

        # Base queryset con prefetch del accessor para evitar N+1
        users_qs = user_model.objects.prefetch_related(accessor_name).all()

        # Determinamos qué campos existen en el modelo usuario para construir búsquedas seguras
        field_names = {f.name for f in user_model._meta.get_fields() if getattr(f, "concrete", False)}

        # Construir filtro de búsqueda sólo con campos disponibles
        if q:
            filtros = Q()
            # campos típicos si tienes modelo Usuario personalizado
            if 'nombre' in field_names:
                filtros |= Q(nombre__icontains=q)
            if 'apellidos' in field_names:
                filtros |= Q(apellidos__icontains=q)
            if 'cedula' in field_names:
                filtros |= Q(cedula__icontains=q)
            if 'rol' in field_names:
                filtros |= Q(rol__icontains=q)

            # si no encontró campos personalizados, buscar por username/email/first_name/last_name
            if not filtros.children:
                if 'username' in field_names:
                    filtros |= Q(username__icontains=q)
                if 'email' in field_names:
                    filtros |= Q(email__icontains=q)
                if 'first_name' in field_names:
                    filtros |= Q(first_name__icontains=q)
                if 'last_name' in field_names:
                    filtros |= Q(last_name__icontains=q)

            users_qs = users_qs.filter(filtros).distinct()

        # Construimos una lista de diccionarios para facilitar render en template
        usuarios_data = []
        for u in users_qs:
            # obtenemos vehículos usando el accessor detectado
            vehiculos = getattr(u, accessor_name).all()
            usuarios_data.append({
                "usuario": u,
                "vehiculos": vehiculos,
            })

        return render(request, "historial/historial.html", {
            "usuarios_data": usuarios_data,
            "query": q,
        })

    # FALLBACK: si no hay FK usuario en Vehiculo mostramos solo vehículos
    else:
        vehiculos = Vehiculo.objects.all()
        if q:
            vehiculos = vehiculos.filter(
                Q(marca__icontains=q) |
                Q(placa__icontains=q) |
                Q(modelo__icontains=q)
            ).distinct()

        return render(request, "historial/historial.html", {
            "vehiculos": vehiculos,
            "query": q,
        })
