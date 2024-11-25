from django.shortcuts import render, redirect
from .forms import CuentaForm
from .models import Cuenta
from django.contrib.auth.decorators import login_required

# Create your views here.



def crear_cuenta(request):
    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cuentas')
    else :
        form = CuentaForm()
    return render(request, 'cuentas/crear_cuenta.html', {'form' : form})

@login_required
def listado_cuentas_cliente(request):

    print(request.user.cliente)

    cliente = request.user.cliente
    cuentas = Cuenta.objects.filter(cliente = cliente)
    return render(request, 'cuentas/listar_cuentas.html', {'cuentas': cuentas})