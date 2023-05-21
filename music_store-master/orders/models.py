from django.db import models
from config import settings
from models.models import Product
from cart.cart import CartItem


class OrderStatus(models.Choices):
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    CANCELLED = ""


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    order_status = models.CharField(max_length=100, choices=OrderStatus.choices, default=OrderStatus.IN_PROGRESS)
    cart_items = models.ManyToManyField(CartItem, related_name='orders')
    email = models.CharField(max_length=150)
    cardHolder = models.CharField(max_length=250)
    cardNo = models.CharField(max_length=250)
    creditExpiry = models.CharField(max_length=30)
    creditCvc = models.CharField(max_length=30)
    billingAddress = models.CharField(max_length=250)
    billingZip = models.IntegerField()
    totalPrice = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"{self.user} - {self.id}"
