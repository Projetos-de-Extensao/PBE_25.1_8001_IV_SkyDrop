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
        fields = ['endereco', 'empresa_nome']

class VendorCreateDeliveryForm(forms.Form):
    recipient = forms.ModelChoiceField(queryset=ClienteUser.objects.all(), label="Recipient (Cliente)")
    weight = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        label="Weight",
        min_value=0.01,
        max_value=15,  # This ensures the value cannot be above 15
        error_messages={'max_value': 'Weight must be 15kg or less.'}
    )
    price = forms.DecimalField(max_digits=8, decimal_places=2, label="Price")
