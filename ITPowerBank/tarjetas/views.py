from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tarjeta
from .forms import TarjetaForm
import random


# Create your views here.

def generar_num():
    numero = [random.randint(0, 9) for _ in range(15)]
    return ''.join(map(str, numero))


@login_required
def solicitar_tarjeta(request):

    cliente = request.user.cliente 
    cvv = str(random.randint(100, 999))
    num = generar_num()

    if request.method == 'POST':
        form = TarjetaForm(request.POST)
        if form.is_valid():
            tarjeta = form.save(commit=False)
            tarjeta.cliente = cliente
            tarjeta.cvv = cvv
            tarjeta.numero = num
            tarjeta.save()
            return redirect('listar_tarjetas')
    else:
        form = TarjetaForm(initial={ 'cliente_nombre': f"{cliente.nombre} {cliente.apellido}" })

    return render(request, 'tarjetas/solicitar_tarjeta.html', {'form': form})

@login_required
def listar_tarjetas(request):
    cliente = request.user.cliente
    tarjeta = Tarjeta.objects.filter(cliente = cliente)

    print(tarjeta)
    return render(request, 'tarjetas/listar_tarjetas.html', {'tarjetas': tarjeta})




