from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def listar_tarjetas(request):
    cliente = request.user.cliente
    tarjeta = cliente.tarjeta_set.all()
    return render(request, 'tarjetas/listar_tarjetas.html', {'tarjeta': tarjeta})