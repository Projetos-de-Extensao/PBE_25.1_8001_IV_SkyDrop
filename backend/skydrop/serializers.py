from rest_framework import serializers
from .models import ClienteUser, VendorUser, PaymentRequest, Drone, Delivery
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ClienteUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ClienteUser
        fields = ['id', 'user', 'endereco', 'telefone']

class VendorUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = VendorUser
        fields = ['id', 'user', 'empresa_nome']

class PaymentRequestSerializer(serializers.ModelSerializer):
    vendor = VendorUserSerializer(read_only=True)
    client = ClienteUserSerializer(read_only=True)
    class Meta:
        model = PaymentRequest
        fields = ['id', 'vendor', 'client', 'price', 'weight', 'status', 'created_at']

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ['id', 'localizacao_atual', 'nivel_bateria', 'status']

class DeliverySerializer(serializers.ModelSerializer):
    payment_request = PaymentRequestSerializer(read_only=True)
    drone = DroneSerializer(read_only=True)
    class Meta:
        model = Delivery
        fields = ['id', 'payment_request', 'drone', 'delivery_status', 'delivery_address', 'delivered_at']
