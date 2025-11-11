from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # ✅ Si es admin, lo manda a Appiniciosoft
            if user.is_superuser:
                return redirect("inicio_admin")
            else:
                return redirect("inicio_usuario")

        else:
            messages.error(request, "⚠️ Usuario o contraseña incorrectos")

    return render(request, "ingresos/login.html")


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect("login")


# SIGNUP
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            messages.error(request, "⚠️ Las contraseñas no coinciden")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ El usuario ya existe")
            return redirect("signup")

        User.objects.create_user(username=username, password=password)
        messages.success(request, "✅ Usuario creado correctamente, inicia sesión")
        return redirect("login")

    return render(request, "ingresos/signup.html")


# INICIO USUARIO
@login_required
def inicio_usuario(request):
    return render(request, "paginas/inicio_usuario.html")
