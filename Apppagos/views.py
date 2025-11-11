from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Pago
from django.db.models import Q

def registrar_pago(request):
    usuarios = Usuario.objects.none()  # nunca None
    usuario_seleccionado = None
    pagos_usuario = []
    mensaje_error = None

    query = (request.GET.get("q") or "").strip()
    usuario_id = request.GET.get("usuario_id") or request.POST.get("usuario_id")

    # Buscar externos si hay query
    if query:
        usuarios = Usuario.objects.filter(
            Q(nombre__icontains=query) |
            Q(apellidos__icontains=query) |
            Q(cedula__icontains=query),
            tipo__iexact="externo"
        )

        if not usuarios.exists():
            mensaje_error = "⚠️ No se encontraron usuarios externos con ese criterio."

    # Seleccionar usuario
    if usuario_id:
        try:
            usuario_seleccionado = get_object_or_404(Usuario, id=usuario_id, tipo__iexact="externo")
            pagos_usuario = Pago.objects.filter(usuario=usuario_seleccionado).order_by('-fecha')
        except (ValueError, Usuario.DoesNotExist):
            mensaje_error = "⚠️ El usuario seleccionado no existe o no es externo."

    # Registrar pago
    if request.method == "POST":
        usuario_id_post = request.POST.get("usuario_id")
        valor = request.POST.get("valor")
        metodo_pago = request.POST.get("metodo_pago")

        if usuario_id_post and valor and metodo_pago:
            usuario_obj = get_object_or_404(Usuario, id=usuario_id_post, tipo__iexact="externo")
            Pago.objects.create(usuario=usuario_obj, valor=valor, metodo_pago=metodo_pago)
            return redirect(f"{request.path}?usuario_id={usuario_obj.id}")

    return render(request, "pagos/pagos.html", {
        "usuarios": usuarios,
        "usuario_seleccionado": usuario_seleccionado,
        "pagos_usuario": pagos_usuario,
        "metodos_pago": Pago.METODOS_PAGO,
        "query": query,
        "mensaje_error": mensaje_error,
    })
