from django.urls import path
from . import views

urlpatterns = [
    # === Usuario ===
    path("usuario/dashboard/", views.usuario_dashboard, name="usuario_dashboard"),
    path("usuario/historial/", views.usuario_historial, name="usuario_historial"),
    path("usuario/perfil/", views.usuario_perfil, name="usuario_perfil"),
    path("usuario/configuracion/", views.usuario_configuracion, name="usuario_configuracion"),
    path("usuario/notificaciones/", views.usuario_notificaciones, name="usuario_notificaciones"),
    path("usuario/soporte/", views.usuario_soporte, name="usuario_soporte"),

    # === Admin Personalizado (adminj/) ===
    path("adminj/dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("adminj/usuarios/", views.admin_usuarios, name="admin_usuarios"),
    path("adminj/vehiculos/", views.admin_vehiculos, name="admin_vehiculos"),
    path("adminj/reportes/", views.admin_reportes, name="admin_reportes"),
    path("adminj/configuracion/", views.admin_configuracion, name="admin_configuracion"),
]
