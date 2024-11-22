from django import forms  # Importamos el módulo de formularios de Django

class LoginForm(forms.Form):  # Creamos un formulario basado en clases
    # Campo para ingresar el nombre de usuario, con un texto de entrada estilizado
    username = forms.CharField(
        label="Usuario",  # Etiqueta que aparecerá junto al campo
        max_length=20,  # Longitud máxima permitida
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Estilo CSS para el campo
    )
    # Campo para ingresar la contraseña, con tipo de entrada "password"
    password = forms.CharField(
        label="Contraseña",  # Etiqueta para el campo
        widget=forms.PasswordInput(attrs={'class': 'form-control'})  # Estilo CSS y entrada oculta
    )
