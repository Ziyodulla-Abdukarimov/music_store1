from django.urls import path
from .views import checkout, my_orders

urlpatterns = [
    path('my-orders/',my_orders, name='my-order'),
    path('checkout/', checkout, name='checkout')
]
