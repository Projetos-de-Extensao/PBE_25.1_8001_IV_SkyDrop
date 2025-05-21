from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestauranteViewSet, ItemMenuViewSet, PedidoViewSet, DroneViewSet

router = DefaultRouter()
router.register(r'restaurantes', RestauranteViewSet)
router.register(r'itens', ItemMenuViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'drones', DroneViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

