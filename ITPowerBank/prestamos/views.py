from django.shortcuts import render
from .forms import PrestamoForm
from django.contrib.auth.decorators import login_required

@login_required
def solicitar_prestamo(request):
    cliente = request.user.cliente  # Relación cliente-usuario autenticado
    tipo_cliente = cliente.tipo_cliente

    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            monto_solicitado = form.cleaned_data.get('monto_solicitado')

            # Límite según tipo de cliente
            limites = {
                'BLACK': 500000,
                'GOLD': 300000,
                'CLASSIC': 100000
            }
            monto_maximo = limites.get(tipo_cliente, 0)

            # Crear el objeto prestamo con valores iniciales
            prestamo = {
                'monto_solicitado': monto_solicitado,
                'estado': 'Rechazado',  # Estado por defecto
                'aprobado': False      # Aprobación por defecto
            }

            if monto_solicitado < monto_maximo:
                # Actualizar el estado si se aprueba
                prestamo['estado'] = 'Aprobado'
                prestamo['aprobado'] = True

                # Guardar el préstamo en la base de datos
                prestamo_x_aprobar = form.save(commit=False)
                prestamo_x_aprobar.cliente = cliente
                prestamo_x_aprobar.monto = monto_solicitado
                prestamo_x_aprobar.save()

            # Renderizar el template con el estado del préstamo
            return render(request, 'prestamos/resultados.html', {'prestamo': prestamo})
    else:
        form = PrestamoForm()

    return render(request, 'prestamos/solicitud.html', {'form': form})
