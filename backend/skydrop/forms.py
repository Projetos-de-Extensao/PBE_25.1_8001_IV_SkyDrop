from django import forms
from django.contrib.auth.models import User
from .models import ClienteUser, VendorUser, PaymentRequest, Delivery

class CustomerCreateRequestForm(forms.Form):
    vendor = forms.ModelChoiceField(queryset=VendorUser.objects.all(), label="Escolha um Vendedor")
    description = forms.CharField(widget=forms.Textarea, label="Descrição do Pedido")

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuário")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")

class CustomerRegisterForm(forms.ModelForm):
    username = forms.CharField(label="Usuário")
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    class Meta:
        model = ClienteUser
        fields = ['endereco', 'telefone']
        labels = {
            'endereco': 'Endereço',
            'telefone': 'Telefone',
        }

class VendorRegisterForm(forms.ModelForm):
    username = forms.CharField(label="Usuário")
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    empresa_nome = forms.CharField(label="Nome da Empresa")
    class Meta:
        model = VendorUser
        fields = ['endereco', 'empresa_nome']
        labels = {
            'endereco': 'Endereço',
            'empresa_nome': 'Nome da Empresa',
        }

class VendorCreateDeliveryForm(forms.Form):
    recipient = forms.ModelChoiceField(queryset=ClienteUser.objects.all(), label="Destinatário (Cliente)")
    description = forms.CharField(
        max_length=255,
        required=False,
        label="Descrição (opcional)",
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descrição do pacote'})
    )
    weight = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        label="Peso (kg)",
        min_value=0.01,
        max_value=15,
        error_messages={'max_value': 'O peso deve ser no máximo 15kg.'}
    )
    price = forms.DecimalField(max_digits=8, decimal_places=2, label="Preço (R$)")

