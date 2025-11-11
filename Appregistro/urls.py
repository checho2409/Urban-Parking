from django.urls import path
from . import views

urlpatterns = [
    path("", views.registro_usuario, name="registro"),
    path("eliminar/<int:vehiculo_id>/", views.eliminar_vehiculo, name="eliminar_vehiculo"),
]
