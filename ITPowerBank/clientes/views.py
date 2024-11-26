from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def infoCliente(request):
    cliente = request.user.cliente
    return render(request, 'clientes/info_cliente.html', {'cliente': cliente})

