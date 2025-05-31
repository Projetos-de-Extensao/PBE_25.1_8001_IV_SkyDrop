from django import forms
from django.contrib.auth.models import User
from .models import ClienteUser, VendorUser, PaymentRequest, Delivery

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CustomerRegisterForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = ClienteUser
        fields = ['endereco', 'telefone']

class VendorRegisterForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    empresa_nome = forms.CharField()
    class Meta:
        model = VendorUser
        fields = ['empresa_nome']

class VendorCreateDeliveryForm(forms.Form):
    recipient = forms.ModelChoiceField(queryset=ClienteUser.objects.all(), label="Recipient (ClienteUser)")
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    weight = forms.DecimalField(max_digits=6, decimal_places=2)
    delivery_address = forms.CharField(max_length=255)
