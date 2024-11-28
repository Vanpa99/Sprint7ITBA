from django import forms
from .models import Tarjeta
from .models import Cliente


class TarjetaForm(forms.ModelForm):
    cliente_nombre = forms.CharField( 
        label="Cliente asociado",
        widget=forms.TextInput(attrs={'class': 'inputField', 'readonly': 'readonly'}),
        required=False,
    )

    class Meta:
        model = Tarjeta
        fields = ['marca', 'tipo'] 
        labels = {
            'Marca': 'Marca de Tarjeta',
            'Tipo': 'Tipo de Tarjeta',
        }
        widgets = {
            'Marca': forms.Select(choices=[('VISA', 'VISA'), ('MASTERCARD', 'MASTERCARD')]),  
            'Tipo': forms.Select(choices=[('DEBITO', 'DEBITO'), ('CREDITO', 'CREDITO')]),  
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = {key: self.fields[key] for key in ['cliente_nombre', *self.fields.keys()]}
