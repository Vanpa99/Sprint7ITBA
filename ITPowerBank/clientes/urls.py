from django.urls import path
from . import views

urlpatterns= [
    path('clientes/info_cliente', views.infoCliente, name='info_cliente')
]