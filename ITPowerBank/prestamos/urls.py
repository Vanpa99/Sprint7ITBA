from django.urls import path
from . import views

urlpatterns = [
    path('solicitar_prestamo/', views.solicitar_prestamo, name='solicitar_prestamo' )

]