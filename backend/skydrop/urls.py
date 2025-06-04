from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    DroneViewSet, DeliveryViewSet, ClienteUserViewSet,
    VendorUserViewSet, PaymentRequestViewSet
)

router = DefaultRouter()
router.register(r'clientes', ClienteUserViewSet)
router.register(r'vendores', VendorUserViewSet)
router.register(r'pagamentos', PaymentRequestViewSet)
router.register(r'drones', DroneViewSet)
router.register(r'entregas', DeliveryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_choice, name='register_choice'),
    path('register/customer/', views.register_customer, name='register_customer'),
    path('register/vendor/', views.register_vendor, name='register_vendor'),
    path('customer/main', views.customer_main, name='customer_main'),
    path('customer/delivery/<int:delivery_id>/', views.customer_delivery_detail, name='customer_delivery_detail'),
    path('vendor/main', views.vendor_main, name='vendor_main'),
    path('vendor/delivery/<int:delivery_id>/', views.vendor_delivery_detail, name='vendor_delivery_detail'),
    path('vendor/create_delivery/', views.vendor_create_delivery, name='vendor_create_delivery'),
]

