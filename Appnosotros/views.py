# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nosotros(request):
    return render(request, 'nosotros/nosotros.html')