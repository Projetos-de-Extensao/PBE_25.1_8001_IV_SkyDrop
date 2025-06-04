from rest_framework import viewsets, permissions
from .models import Drone, Delivery, ClienteUser, VendorUser, PaymentRequest
from .serializers import (
    DroneSerializer, DeliverySerializer, ClienteUserSerializer, VendorUserSerializer, PaymentRequestSerializer
)
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, CustomerRegisterForm, VendorRegisterForm, VendorCreateDeliveryForm
from django.contrib.auth.models import User
from django.db import transaction
from django.urls import reverse


class DroneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [permissions.IsAuthenticated]

class ClienteUserViewSet(viewsets.ModelViewSet):
    queryset = ClienteUser.objects.all()
    serializer_class = ClienteUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class VendorUserViewSet(viewsets.ModelViewSet):
    queryset = VendorUser.objects.all()
    serializer_class = VendorUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentRequestViewSet(viewsets.ModelViewSet):
    queryset = PaymentRequest.objects.all()
    serializer_class = PaymentRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def create_payment_request(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            with transaction.atomic():
                payment_request = serializer.save()
                return Response(self.get_serializer(payment_request).data, status=201)
        return Response(serializer.errors, status=400)

def home(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'clienteuser'):
            return redirect('customer_main')
        elif hasattr(request.user, 'vendoruser'):
            return redirect('vendor_main')
    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                # Redirect based on user type
                if hasattr(user, 'clienteuser'):
                    return redirect('customer_main')
                elif hasattr(user, 'vendoruser'):
                    return redirect('vendor_main')
                else:
                    return redirect('home')
        return render(request, 'login.html', {'form': form, 'error': 'Credenciais inválidas'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                cliente = ClienteUser.objects.create(
                    user=user,
                    endereco=form.cleaned_data['endereco'],
                    telefone=form.cleaned_data['telefone']
                )
                login(request, user)
                return redirect('customer_main')
    else:
        form = CustomerRegisterForm()
    return render(request, 'customer_register.html', {'form': form})

def register_vendor(request):
    if request.method == 'POST':
        form = VendorRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            endereco = form.cleaned_data['endereco']
            empresa_nome = form.cleaned_data['empresa_nome']

            user = User.objects.create_user(username=username, email=email, password=password)
            VendorUser.objects.create(user=user, endereco=endereco, empresa_nome=empresa_nome)
            return redirect('vendor_main')
    else:
        form = VendorRegisterForm()
    return render(request, 'vendor_register.html', {'form': form})

@login_required
def customer_main(request):
    if not hasattr(request.user, 'clienteuser'):
        return redirect('home')
    deliveries = Delivery.objects.filter(payment_request__client=request.user.clienteuser)
    active = deliveries.filter(delivery_status__in=['pendente', 'entregando', 'confirmado'])
    past = deliveries.filter(delivery_status__in=['entregue', 'cancelado'])
    return render(request, 'customer_main.html', {'active_deliveries': active, 'past_deliveries': past})

@login_required
def customer_delivery_detail(request, delivery_id):
    if not hasattr(request.user, 'clienteuser'):
        return redirect('home')
    delivery = get_object_or_404(Delivery, id=delivery_id, payment_request__client=request.user.clienteuser)
    if request.method == 'POST':
        # Pay
        if 'pay' in request.POST and delivery.payment_request.status == 'pendente':
            delivery.payment_request.status = 'pago'
            delivery.payment_request.save()
            delivery.delivery_status = 'confirmado'
            delivery.save()
        
        elif 'cancel' in request.POST and delivery.payment_request.status == 'pendente':
            delivery.payment_request.status = 'cancelado'
            delivery.payment_request.save()
            delivery.delivery_status = 'cancelado'
            if delivery.drone:
                delivery.drone.status = 'disponivel'
                delivery.drone.save()

        elif 'confirm' in request.POST and delivery.delivery_status == 'entregando':
            delivery.delivery_status = 'entregue'
            delivery.save()
            if delivery.drone:
                delivery.drone.status = 'disponivel'
                delivery.drone.save()
    
        return redirect('customer_delivery_detail', delivery_id=delivery.id)
    
    return render(request, 'customer_delivery_detail.html', {'delivery': delivery})

@login_required
def vendor_main(request):
    if not hasattr(request.user, 'vendoruser'):
        return redirect('home')
    deliveries = Delivery.objects.filter(payment_request__vendor=request.user.vendoruser)
    active = deliveries.filter(delivery_status__in=['pendente', 'entregando', 'confirmado'])
    past = deliveries.filter(delivery_status__in=['entregue', 'cancelado'])
    return render(request, 'vendor_main.html', {'active_deliveries': active, 'past_deliveries': past})

@login_required
def vendor_delivery_detail(request, delivery_id):
    if not hasattr(request.user, 'vendoruser'):
        return redirect('home')
    delivery = get_object_or_404(Delivery, id=delivery_id, payment_request__vendor=request.user.vendoruser)
    error = None

    if request.method == 'POST':
        # Assign drone if payment is paid and delivery is pending
        if 'send_drone' in request.POST and delivery.payment_request.status == 'pago' and delivery.delivery_status == 'confirmado':
            available_drone = Drone.objects.filter(status='disponivel').first()
            if available_drone:
                delivery.drone = available_drone
                delivery.delivery_status = 'entregando'
                delivery.save()
                available_drone.status = 'entregando'
                available_drone.save()
            else:
                error = "Não há drones disponíveis no momento."
        
        return redirect('vendor_delivery_detail', delivery_id=delivery.id)
    
    return render(request, 'vendor_delivery_detail.html', {'delivery': delivery, 'error': error})

@login_required
def vendor_create_delivery(request):
    if not hasattr(request.user, 'vendoruser'):
        return redirect('home')
    if request.method == 'POST':
        form = VendorCreateDeliveryForm(request.POST)
        if form.is_valid():
            # Create PaymentRequest
            payment_request = PaymentRequest.objects.create(
                vendor=request.user.vendoruser,
                client=form.cleaned_data['recipient'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                weight=form.cleaned_data['weight'],
                status='pendente'
            )
            # Create Delivery
            cliente = form.cleaned_data['recipient']
            delivery = Delivery.objects.create(
                payment_request=payment_request,
                delivery_status='pendente',
                delivery_address=cliente.endereco  # Use the selected client's address
            )
            return redirect('vendor_delivery_detail', delivery_id=delivery.id)
    else:
        form = VendorCreateDeliveryForm()

    return render(request, 'vendor_create_delivery.html', {'form': form})

def register_choice(request):
    return render(request, 'register_choice.html')