from django import forms
from .models import Pedido, ItemMenu

class PedidoForm(forms.ModelForm):
    itens = forms.ModelMultipleChoiceField(
        queryset=ItemMenu.objects.none(),  # set dynamically
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Pedido
        fields = ['itens']

    def __init__(self, restaurante, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['itens'].queryset = restaurante.cardapio.all()
