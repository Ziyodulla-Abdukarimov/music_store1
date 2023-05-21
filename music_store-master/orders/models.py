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


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.order.user}: {self.product.name}'
