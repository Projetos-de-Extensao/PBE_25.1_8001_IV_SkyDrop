from django.db import models

class Produto (models.Model):
    nome = models.CharField(max_lenghth=100)
    preco = models.CharField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    disponivel = models.booleanField(default=True)

    def __str__(self):
        return self.nome
# Create your models here.
