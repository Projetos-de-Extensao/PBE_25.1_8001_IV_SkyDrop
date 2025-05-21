from rest_framework import serializers
from .models import Restaurante, ItemMenu, Pedido, Drone
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ItemMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMenu
        fields = ['id', 'nome', 'preco']

class RestauranteSerializer(serializers.ModelSerializer):
    cardapio = ItemMenuSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurante
        fields = ['id', 'nome', 'localizacao', 'cardapio']

class PedidoSerializer(serializers.ModelSerializer):
    itens = serializers.PrimaryKeyRelatedField(queryset=ItemMenu.objects.all(), many=True)
    usuario = serializers.ReadOnlyField(source='usuario.username')

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'restaurante', 'itens', 'preco_total', 'status', 'drone_atribuido']

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ['id', 'localizacao_atual', 'nivel_bateria', 'status']
