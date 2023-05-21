from django.contrib import admin
from .models import Order, OrderItems

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItems)
