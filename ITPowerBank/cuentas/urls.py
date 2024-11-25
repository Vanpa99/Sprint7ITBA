from django.urls import path
from . import views

urlpatterns= [
    path('registrar_cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('listar_cuentas/', views.listado_cuentas_cliente, name='listar_cuentas'),
]