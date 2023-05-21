from django.db import models
from common.models import BaseModel
from config import settings
from models.models import Product
from django.db.models import F, Sum


# Create your models here.
class UserCart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart', blank=True,
                                null=True)
    cart_id_pk = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class StatusChoice(models.TextChoices):
    ACTIVE = "active"
    INACTIVE = 'inactive'


class CartItem(BaseModel):
    cart = models.ForeignKey(UserCart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=8, choices=StatusChoice.choices, default=StatusChoice.ACTIVE)

    @staticmethod
    def get_total_price():
        return CartItem.objects.annotate(item_price=F('product__price') * F('quantity')).aggregate(
            total_price=Sum('item_price'))['total_price'] or 0

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return str(self.product)
