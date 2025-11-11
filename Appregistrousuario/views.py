from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import UsuarioForm
from .models import Usuario

def registro_usuario(request):
    query = request.GET.get('q')
    if query:
        usuarios = Usuario.objects.filter(
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(documento__icontains=query)
        ).order_by('-creado_en')
    else:
        usuarios = Usuario.objects.all().order_by('-creado_en')

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_usuario')
    else:
        form = UsuarioForm()

    return render(request, 'usuario/usuarios.html', {
        'form': form,
        'usuarios': usuarios,
        'query': query if query else ''
    })
