from django.urls import path
from . import views


urlpatterns = [
    path('tarjetas/', views.listar_tarjetas, name='listar_tarjetas' )
]