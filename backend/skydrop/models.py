from django.contrib.auth.models import User
from django.db import models

class ClienteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f"Cliente {self.user.username}"


class VendorUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=255)
    empresa_nome = models.CharField(max_length=255)

    def __str__(self):
        return f"Vendedor {self.user.username}"


class PaymentRequest(models.Model):
    vendor = models.ForeignKey(VendorUser, on_delete=models.CASCADE)
    client = models.ForeignKey(ClienteUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pagamento #{self.id} - {self.status}"


class Drone(models.Model):
    localizacao_atual = models.CharField(max_length=255)
    nivel_bateria = models.FloatField()
    status = models.CharField(max_length=50, choices=[
        ('disponivel', 'Disponível'),
        ('entregando', 'Entregando'),
        ('carregando', 'Carregando')
    ])

    def __str__(self):
        return f"Drone #{self.id} - {self.status}"

    def atribuir_entrega(self, pedido):
        # lógica para atribuir pedido
        pass

    def atualizar_localizacao(self, nova_localizacao):
        self.localizacao_atual = nova_localizacao
        self.save()

    def verificar_bateria(self):
        return self.nivel_bateria

    def recarregar(self):
        # lógica de recarga
        pass


class Delivery(models.Model):
    payment_request = models.OneToOneField(PaymentRequest, on_delete=models.CASCADE)
    drone = models.ForeignKey(Drone, null=True, blank=True, on_delete=models.SET_NULL)
    delivery_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('delivered', 'Delivered'),
        ('confirmed', 'Confirmed')
    ])
    delivery_address = models.CharField(max_length=255)
    delivered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Entrega #{self.id} - {self.delivery_status}"
