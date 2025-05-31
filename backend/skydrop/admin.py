from django.contrib import admin
from .models import ClienteUser, VendorUser, PaymentRequest, Drone, Delivery

admin.site.register(ClienteUser)
admin.site.register(VendorUser)
admin.site.register(PaymentRequest) 
admin.site.register(Drone)
admin.site.register(Delivery)