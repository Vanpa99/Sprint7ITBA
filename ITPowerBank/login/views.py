from django.shortcuts import render, redirect  # Funciones para renderizar plantillas y redirigir
from django.contrib.auth import authenticate, login  # Funciones para autenticar y registrar sesiones
from .forms import LoginForm,RegistroForm  # Importamos el formulario que acabamos de definir
from django.contrib.auth.models import User  # Modelo de usuarios
from clientes.models import Cliente  # Importamos el modelo Cliente
from django.contrib.auth.decorators import login_required  # Decorador para proteger vistas
from django.db import IntegrityError  # Para capturar errores de la base de datos
from django.contrib import messages  # Para mostrar mensajes al usuario

# Create your views here.

def login_view(request):  # Vista que maneja el inicio de sesión
    if request.method == 'POST':  # Si la solicitud es de tipo POST (envío de formulario)
        form = LoginForm(request.POST)  # Cargamos los datos enviados al formulario
        if form.is_valid():  # Verificamos que los datos sean válidos
            # Extraemos los datos validados del formulario
            username = form.cleaned_data['username']  
            password = form.cleaned_data['password']
            # Intentamos autenticar al usuario con las credenciales proporcionadas
            user = authenticate(request, username=username, password=password)
            if user is not None:  # Si las credenciales son correctas y el usuario existe
                login(request, user)  # Inicia sesión para el usuario
                return redirect('home')  # Redirige al usuario a la página principal (home banking)
            else:
                # Si la autenticación falla, agregamos un mensaje de error al formulario
                form.add_error(None, "Usuario o contraseña incorrectos")
    else:  # Si la solicitud es de tipo GET (carga inicial de la página)
        form = LoginForm()  # Creamos un formulario vacío para mostrarlo en la plantilla
    # Renderizamos la plantilla con el formulario (vacío o con errores)
    return render(request, 'login/login.html', {'form': form})

@login_required
def home_view(request):  # Vista protegida para el home
    return render(request, 'home.html')  # Renderiza el archivo templates/home.html

from django.db import IntegrityError
from django.contrib import messages

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Crear usuario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Intentar crear cliente asociado al usuario
            try:
                Cliente.objects.create(
                    user=user,
                    nombre=form.cleaned_data['nombre'],
                    apellido=form.cleaned_data['apellido'],
                    dni=form.cleaned_data['dni']
                )
                return redirect('login')  # Redirigir al login después del registro exitoso
            except IntegrityError:
                messages.error(request, "El DNI ingresado ya está registrado. Por favor, intenta con otro.")
    else:
        form = RegistroForm()
    return render(request, 'login/registro.html', {'form': form})
