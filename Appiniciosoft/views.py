from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def inicio_admin(request):
    hora = datetime.now().hour
    if hora < 12:
        saludo = "¡Buenos días"
    elif hora < 18:
        saludo = "¡Buenas tardes"
    else:
        saludo = "¡Buenas noches"

    return render(request, "soft/softw.html", {
        "usuario": request.user,
        "saludo": saludo,
    })
