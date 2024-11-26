from django import forms
from .models import Cuenta

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['cliente', 'saldo', 'numero', 'tipo']
        label = {
            'numero': 'Numero de cuenta',
            'saldo': 'Saldo inicial',
            'numero': 'Numero de cuenta',
            'cliente': 'Cliente asociado',
        }
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'saldo': forms.NumberInput(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }