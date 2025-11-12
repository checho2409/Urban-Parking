from django.shortcuts import render, get_object_or_404, redirect

def lista_ingresos(request):
    return render(request, "inveh/lista.html")
