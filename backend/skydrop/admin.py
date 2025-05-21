from django.contrib import admin
from .models import Restaurante, ItemMenu, Drone, Pedido, Perfil

admin.site.register(Restaurante)
admin.site.register(ItemMenu)
admin.site.register(Drone)
admin.site.register(Pedido)
admin.site.register(Perfil)