from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='asd')
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='products',
    )
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='product/')
    description = RichTextField()
    country = models.CharField(max_length=250)
    qty = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    code = models.CharField(max_length=50)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name