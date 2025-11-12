from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ingresos, name='lista'),  # 👈 esta línea nueva
    path("lista/", views.lista_ingresos, name="lista_ingresos"),]
