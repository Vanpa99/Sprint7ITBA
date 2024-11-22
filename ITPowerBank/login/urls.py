from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login_view, name='login'),  # Página principal de login
    path('home/', views.home_view, name='home'),  # Página protegida de inicio
    path('registro/', views.registro_view, name='registro'),  # Página de registro
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]