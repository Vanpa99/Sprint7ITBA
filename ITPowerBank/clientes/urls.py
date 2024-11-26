from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns= [
    path('info_cliente', login_required(views.infoCliente), name='info_cliente')
]