from django.contrib import admin
from .models import Cuenta, TipoCuenta
# Register your models here.

admin.site.register(Cuenta)
admin.site.register(TipoCuenta)