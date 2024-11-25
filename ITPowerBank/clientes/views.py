from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    return render(request, 'home.html')


def infoCliente(request):
    cliente = request.user.cliente
    return render(request, 'clientes/info_cliente.html', {'cliente': cliente})

