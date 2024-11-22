from django.shortcuts import render, redirect  # Funciones para renderizar plantillas y redirigir
from django.contrib.auth import authenticate, login  # Funciones para autenticar y registrar sesiones
from .forms import LoginForm  # Importamos el formulario que acabamos de definir

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
                return redirect('/')  # Redirige al usuario a la página principal (home banking)
            else:
                # Si la autenticación falla, agregamos un mensaje de error al formulario
                form.add_error(None, "Usuario o contraseña incorrectos")
    else:  # Si la solicitud es de tipo GET (carga inicial de la página)
        form = LoginForm()  # Creamos un formulario vacío para mostrarlo en la plantilla
    # Renderizamos la plantilla con el formulario (vacío o con errores)
    return render(request, 'login/login.html', {'form': form})
