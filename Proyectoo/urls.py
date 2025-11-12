from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # apps
    path("", include("Appingreso.urls")),  
    path('', include('Appinicio.urls')),      
    path('informacion/', include('Appinformacion.urls')),
    path('historial/', include('Apphistorial.urls')), 
    path('pagos/', include('Apppagos.urls')),
    path('registro/', include('Appregistro.urls')),
    path("iniciosoft/", include("Appiniciosoft.urls")),
    path("ingresos-vehiculos/", include("Appingreso_vehiculos.urls")),
    path("nosotros/", include("Appnosotros.urls")),
    path('perfil/', include('Appperfil.urls')),
    path('usuarios/', include('Appregistrousuario.urls')), 
    path("", include("Appcrearcuenta.urls")),
    path('', include('parking.urls')),
]
