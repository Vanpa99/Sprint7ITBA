from django.shortcuts import render
from .models import Tarjeta 
# Create your views here.

def listar_tarjetas(request):
    cliente = request.user.cliente
    tarjeta = Tarjeta.objects.filter(cliente = cliente)
    return render(request, 'tarjetas/listar_tarjetas.html', {'tarjeta': tarjeta})