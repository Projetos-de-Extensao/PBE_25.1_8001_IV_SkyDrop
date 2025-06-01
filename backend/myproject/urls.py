"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, re_path, include
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from skydrop.views import ClienteUserViewSet, VendorUserViewSet, PaymentRequestViewSet, DroneViewSet, DeliveryViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="SkyDrop API",
        default_version='v1',
        description="Documentação da API para o sistema de entrega de alimentos movido a drones",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="Back End License"),
    ),
    public=True,
    permission_classes=(IsAuthenticated,),
)

router = DefaultRouter()
router.register(r'clientes', ClienteUserViewSet)
router.register(r'vendores', VendorUserViewSet)
router.register(r'pagamentos', PaymentRequestViewSet)
router.register(r'drones', DroneViewSet)
router.register(r'entregas', DeliveryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('skydrop.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui()),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', lambda request: redirect('login')),
    path('', include(router.urls)),
]
