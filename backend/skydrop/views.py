from rest_framework import viewsets, permissions
from .models import Restaurante, ItemMenu, Pedido, Drone
from .serializers import RestauranteSerializer, ItemMenuSerializer, PedidoSerializer, DroneSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import render, get_object_or_404
from .forms import PedidoForm
from django.contrib.auth.decorators import login_required
from django.db import transaction



class RestauranteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class ItemMenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemMenu.objects.all()
    serializer_class = ItemMenuSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        pedido = serializer.save(usuario=self.request.user)
        # Calculate total
        total = sum(item.preco for item in pedido.itens.all())
        pedido.preco_total = total
        pedido.save()

        # Assign drone
        drone = Drone.objects.filter(status='disponivel').first()
        if drone:
            pedido.drone_atribuido = drone
            drone.status = 'entregando'
            drone.save()
            pedido.save()

class DroneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

def ver_cardapio(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, id=restaurante_id)
    itens = restaurante.cardapio.all()
    return render(request, 'ver_cardapio.html', {'restaurante': restaurante, 'itens': itens})

@login_required
@transaction.atomic
def fazer_pedido(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, id=restaurante_id)

    if request.method == 'POST':
        form = PedidoForm(restaurante, request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.restaurante = restaurante
            pedido.status = 'realizado'

            # Calculate total
            pedido.preco_total = sum(item.preco for item in form.cleaned_data['itens'])

            # Assign available drone
            drone = Drone.objects.filter(status='disponivel').first()
            if drone:
                pedido.drone_atribuido = drone
                drone.status = 'entregando'
                drone.save()

            pedido.save()
            form.save_m2m()

            return render(request, 'pedido_confirmado.html', {'pedido': pedido})
    else:
        form = PedidoForm(restaurante)

    return render(request, 'fazer_pedido.html', {'form': form, 'restaurante': restaurante})