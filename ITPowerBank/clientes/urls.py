from django.urls import path
from . import views

urlpatterns= [
    path('clientes/<int:cliente_id>/', views.datos_cliente, name='mostrar_datos')
]