from django.urls import path
from . import views
urlpatterns= [
    path('info_cliente', views.infoCliente, name='info_cliente')
]