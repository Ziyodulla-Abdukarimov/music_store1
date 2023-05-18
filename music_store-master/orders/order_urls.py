from django.urls import path
from .views import checkout

urlpatterns = [
    path('checkout/', checkout, name='checkout')
]
