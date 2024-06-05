from django.db import models
from django.contrib.auth.models import AbstractUser


class CircularUser(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        app_label = 'user_'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='circular_users',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted '
    )


class Meta:
    permissions = [
        ("view_user", "View user"),
    ]
