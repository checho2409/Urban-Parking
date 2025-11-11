from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime

# ======================================================
# === Vistas Usuario ===
# ======================================================
@login_required
def usuario_dashboard(request):
    return render(request, "usuario/usuario_dashboard.html", {"usuario": request.user})

@login_required
def usuario_historial(request):
    return render(request, "usuario/usuario_historial.html", {"usuario": request.user})

@login_required
def usuario_perfil(request):
    return render(request, "usuario/usuario_perfil.html", {"usuario": request.user})

@login_required
def usuario_configuracion(request):
    return render(request, "usuario/usuario_configuracion.html", {"usuario": request.user})

@login_required
def usuario_notificaciones(request):
    return render(request, "usuario/usuario_notificaciones.html", {"usuario": request.user})

@login_required
def usuario_soporte(request):
    return render(request, "usuario/usuario_soporte.html", {"usuario": request.user})


# ======================================================
# === Función para saludo dinámico (Admin) ===
# ======================================================
def obtener_saludo():
    hora = datetime.now().hour
    if hora < 12:
        return "Buenos días"
    elif hora < 18:
        return "Buenas tardes"
    return "Buenas noches"


# ======================================================
# === Vistas Admin Personalizado ===
# ======================================================
@login_required
def admin_dashboard(request):
    return render(request, "adminj/admin_dashboard.html", {
        "usuario": request.user,
        "saludo": obtener_saludo(),
    })

@login_required
def admin_usuarios(request):
    return render(request, "adminj/admin_usuarios.html", {
        "usuario": request.user,
        "saludo": obtener_saludo(),
    })

@login_required
def admin_vehiculos(request):
    return render(request, "adminj/admin_vehiculos.html", {
        "usuario": request.user,
        "saludo": obtener_saludo(),
    })

@login_required
def admin_reportes(request):
    return render(request, "adminj/admin_reportes.html", {
        "usuario": request.user,
        "saludo": obtener_saludo(),
    })

@login_required
def admin_configuracion(request):
    return render(request, "adminj/admin_configuracion.html", {
        "usuario": request.user,
        "saludo": obtener_saludo(),
    })

from django.shortcuts import render
from .forms import ConfiguracionForm

def configuracion_view(request):
    if request.method == 'POST':
        form = ConfiguracionForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = 'Configuración guardada correctamente.'
            return render(request, 'adminpanel/configuracion.html', {
                'form': form,
                'mensaje': mensaje
            })
    else:
        form = ConfiguracionForm(initial={'nombre': 'AdminSoft', 'email': 'admin@soft.com'})
    return render(request, 'adminpanel/configuracion.html', {'form': form})

from django.shortcuts import render
from .forms import PerfilUsuarioForm

def perfil_usuario_view(request):
    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            telefono = form.cleaned_data['telefono']
            mensaje = 'Perfil actualizado correctamente.'
            return render(request, 'usuariopanel/perfil.html', {
                'form': form,
                'mensaje': mensaje
            })
    else:
        form = PerfilUsuarioForm(initial={'nombre': 'Juan Pérez', 'telefono': '3001234567'})
    return render(request, 'usuariopanel/perfil.html', {'form': form})
