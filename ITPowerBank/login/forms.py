from django import forms  # Importamos el módulo de formularios de Django
from django.contrib.auth.models import User  # Para trabajar con el modelo de usuarios
from django.core.exceptions import ValidationError  # Para manejar errores personalizados
from clientes.models import Cliente  # Importamos el modelo Cliente

class LoginForm(forms.Form):  # Creamos un formulario basado en clases
    # Campo para ingresar el nombre de usuario, con un texto de entrada estilizado
    username = forms.CharField(
        label="Usuario",  # Etiqueta que aparecerá junto al campo
        max_length=20,  # Longitud máxima permitida
        widget=forms.TextInput(attrs={'class': 'inputField'})  # Estilo CSS para el campo
    )
    # Campo para ingresar la contraseña, con tipo de entrada "password"
    password = forms.CharField(
        label="Contraseña",  # Etiqueta para el campo
        widget=forms.PasswordInput(attrs={'class': 'inputField'})  # Estilo CSS y entrada oculta
    )

class RegistroForm(forms.Form):
    username = forms.CharField(
        max_length=150, 
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={'class': 'inputField'})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'inputField'}), 
        label="Contraseña"
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'inputField'}), 
            label="Repite la contraseña"
    )
    
    nombre = forms.CharField(
        max_length=100, 
        label="Nombre",
        widget=forms.TextInput(attrs={'class': 'inputField'})
    )

    apellido = forms.CharField(
        max_length=100, 
        label="Apellido",
        widget=forms.TextInput(attrs={'class': 'inputField'})
    )

    dni = forms.CharField(
        max_length=10, 
        label="DNI",
        widget=forms.TextInput(attrs={'class': 'inputField'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Usuario no disponible, intenta con otro.")
        return username

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if Cliente.objects.filter(dni=dni).exists():
            raise forms.ValidationError("Este DNI ya ha sido utilizado, comprueba si ya has creado una cuenta con anterioridad.")
        return dni

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data