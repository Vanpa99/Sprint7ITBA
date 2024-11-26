from django import forms
from .models import Prestamos
from django.contrib.auth.models import User

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamos
        fields = ['tipo', 'fecha']

    monto_solicitado = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
        label="Monto Solicitado"
    )

    def clean(self):
        cleaned_data = super().clean()
        monto_solicitado = cleaned_data.get('monto')
        tipo_cliente = self.initial.get('tipo_cliente')  # Pasado desde la vista

        # Definir el monto máximo según el tipo de cliente
        limites = {
            'BLACK': 500000,
            'GOLD': 300000,
            'CLASSIC': 100000
        }
        monto_maximo = limites.get(tipo_cliente, 0)

        # Verificar si el monto solicitado excede el permitido
        if monto_solicitado and monto_solicitado > monto_maximo:
            raise forms.ValidationError(
                f"El monto solicitado ({monto_solicitado}) excede el límite permitido para el cliente {tipo_cliente} ({monto_maximo})."
            )

        return cleaned_data