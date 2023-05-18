from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
ADMIN, MANAGER, CLIENT = (
    "admin",
    "manager",
    "client"
)


class MybaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MyUser(AbstractUser):
    USER_ROLE = (
        (ADMIN, ADMIN),
        (MANAGER, MANAGER),
        (CLIENT, CLIENT)
    )
    user_role = models.CharField(max_length=10, choices=USER_ROLE, default=CLIENT)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
