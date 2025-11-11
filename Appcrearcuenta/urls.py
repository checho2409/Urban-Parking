from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("crear/", views.crear_cuenta, name="crear_cuenta"),
    path("exitoso/", TemplateView.as_view(template_name="Appcrearcuenta/registro_exitoso.html"), name="registro_exitoso"),
]
