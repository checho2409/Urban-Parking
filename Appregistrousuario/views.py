from django.shortcuts import render, redirect
from django.db.models import Q

def registro_usuario(request):
    return render(request, 'usuario/usuarios.html')
