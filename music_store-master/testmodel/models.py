from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self',
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
