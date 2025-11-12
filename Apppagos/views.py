from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q


def pagos(request):
    return render(request,"pagos/pagos.html")
