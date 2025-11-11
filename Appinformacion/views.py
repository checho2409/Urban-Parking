from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def informacion (request):
    return render(request, 'paginas2/informe.html')


def base (request):
    return render(request, 'paginas/base.html')

