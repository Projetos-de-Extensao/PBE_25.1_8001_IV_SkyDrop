from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

    def fazer_pedido(self, detalhes_pedido):
        # lógica para criar pedido
        pass

    def rastrear_pedido(self, id_pedido):
        # lógica para rastrear pedido
        pass

    def atualizar_perfil(self, novas_infos):
        # lógica para atualizar informações
        pass


class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    def preparar_pedido(self, id_pedido):
        # lógica para preparar pedido
        pass

    def atualizar_cardapio(self, item, acao):
        # lógica para adicionar/remover item do cardápio
        pass

    def obter_cardapio(self):
        return self.cardapio.all()


class ItemMenu(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    restaurante = models.ForeignKey(Restaurante, related_name='cardapio', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - R${self.preco}"


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


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('realizado', 'Realizado'),
        ('preparando', 'Preparando'),
        ('a_caminho', 'A Caminho'),
        ('entregue', 'Entregue')
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    itens = models.ManyToManyField(ItemMenu)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    drone_atribuido = models.ForeignKey(Drone, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Pedido #{self.id} - {self.status}"

    def atualizar_status(self, novo_status):
        self.status = novo_status
        self.save()

    def calcular_total(self):
        total = sum(item.preco for item in self.itens.all())
        self.preco_total = total
        self.save()
        return total

    def atribuir_drone(self, drone):
        self.drone_atribuido = drone
        self.save()

    def obter_detalhes_pedido(self):
        return {
            "usuario": self.usuario.nome,
            "itens": list(self.itens.values_list('nome', flat=True)),
            "total": self.preco_total,
            "status": self.status,
            "drone": self.drone_atribuido.id if self.drone_atribuido else None
        }
