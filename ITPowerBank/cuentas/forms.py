from django import forms
from .models import Cuenta

# class CuentaForm(forms.ModelForm):
#     class Meta:
#         model = Cuenta
#         fields = ['saldo', 'numero', 'tipo']  # Eliminamos 'cliente' porque lo manejamos dinámicamente
#         labels = {
#             'numero': 'Número de cuenta',
#             'saldo': 'Saldo inicial',
#             'tipo': 'Tipo de cuenta',
#         }
#         widgets = {
#             'numero': forms.TextInput(attrs={'class': 'inputField'}),
#             'tipo': forms.Select(attrs={'class': 'inputField'}),
#             'saldo': forms.NumberInput(attrs={'class': 'inputField'}),
#         }

#     cliente_nombre = forms.CharField(  # Campo solo para mostrar el cliente
#         label="Cliente asociado",
#         widget=forms.TextInput(attrs={'class': 'inputField', 'readonly': 'readonly'}),
#         required=False,
#     )

from django import forms
from .models import Cuenta

class CuentaForm(forms.ModelForm):
    cliente_nombre = forms.CharField(  # Campo adicional para mostrar el cliente
        label="Cliente asociado",
        widget=forms.TextInput(attrs={'class': 'inputField', 'readonly': 'readonly'}),
        required=False,
    )

    class Meta:
        model = Cuenta
        fields = ['saldo', 'numero', 'tipo']  # Campos originales
        labels = {
            'numero': 'Número de cuenta',
            'saldo': 'Saldo inicial',
            'tipo': 'Tipo de cuenta',
        }
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'inputField'}),
            'tipo': forms.Select(attrs={'class': 'inputField'}),
            'saldo': forms.NumberInput(attrs={'class': 'inputField'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Reorganizamos el orden de los campos, colocando 'cliente_nombre' al principio
        self.fields = {key: self.fields[key] for key in ['cliente_nombre', *self.fields.keys()]}
