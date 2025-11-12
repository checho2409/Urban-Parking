from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagos, name='registrar_pago'),  # /pagos/
]
