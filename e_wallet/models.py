from django.db import models
from django.utils import timezone
from user_.models import CircularUser


class Wallet(models.Model):
    user = models.OneToOneField(CircularUser, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, default='NGN')
    pin = models.CharField(max_length=4, default='0000')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
