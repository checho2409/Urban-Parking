from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ingresos, name='lista'),  # 👈 esta línea nueva
    path("lista/", views.lista_ingresos, name="lista_ingresos"),
    path("nuevo/", views.registrar_ingreso, name="registrar_ingreso"),
    path("salida/<int:id>/", views.registrar_salida, name="registrar_salida"),  # salida directa
]

