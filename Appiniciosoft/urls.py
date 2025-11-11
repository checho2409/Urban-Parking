from django.urls import path
from . import views

urlpatterns = [
    path("admin-inicio/", views.inicio_admin, name="inicio_admin"),
]
