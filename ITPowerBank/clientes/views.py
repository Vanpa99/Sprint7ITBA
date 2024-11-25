from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from clientes.models import Cliente
# Create your views here.

@login_required
def home_view(request):
    return render(request, 'home.html')



def datos_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/info_cliente.html', {'cliente': cliente})

