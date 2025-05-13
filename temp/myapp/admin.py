from django.contrib import admin
from .models import Usuario, Restaurante, ItemMenu, Drone, Pedido

admin.site.register(Usuario)
admin.site.register(Restaurante)
admin.site.register(ItemMenu)
admin.site.register(Drone)
admin.site.register(Pedido)