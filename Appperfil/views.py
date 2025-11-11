from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Perfil

@login_required
def perfil_usuario(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'perfil/perfil.html', {'perfil': perfil})
