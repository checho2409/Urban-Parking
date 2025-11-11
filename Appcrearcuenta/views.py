from django.shortcuts import render, redirect
from .forms import CrearCuentaForm

def crear_cuenta(request):
    if request.method == "POST":
        form = CrearCuentaForm(request.POST)
        if form.is_valid():
            form.save()
            print("✅ Usuario creado correctamente")
            return redirect("registro_exitoso")  # Te manda a la página de éxito
        else:
            print("❌ Errores en el formulario:", form.errors)
    else:
        form = CrearCuentaForm()

    return render(request, "Appcrearcuenta/crear_cuenta.html", {"form": form})
