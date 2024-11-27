from django.shortcuts import render, redirect
from .forms import CuentaForm
from .models import Cuenta
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def crear_cuenta(request):
    cliente = request.user.cliente  # Obtener cliente asociado al usuario logueado
    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            cuenta = form.save(commit=False)  # Crear instancia pero no guardar todavía
            cuenta.cliente = cliente  # Asignar el cliente automáticamente
            cuenta.save()
            return redirect('listar_cuentas')  # Redirigir a la lista de cuentas
    else:
        form = CuentaForm(initial={'cliente_nombre': f"{cliente.nombre} {cliente.apellido}"})
    return render(request, 'cuentas/crear_cuenta.html', {'form': form})

@login_required
def listado_cuentas_cliente(request):

    print(request.user.cliente)

    cliente = request.user.cliente
    cuentas = Cuenta.objects.filter(cliente = cliente)
    return render(request, 'cuentas/listar_cuentas.html', {'cuentas': cuentas})