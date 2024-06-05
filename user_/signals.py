from django.db.models.signals import post_save
from django.dispatch import receiver
from user_.models import CircularUser
from e_wallet.models import Wallet


@receiver(post_save, sender=CircularUser)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)
