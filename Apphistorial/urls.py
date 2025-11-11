from django.urls import path
from .views import historial_view

urlpatterns = [
    path('', historial_view, name='historial'),
]
