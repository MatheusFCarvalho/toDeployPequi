from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TIPOS_USUARIO = [
        ('vendedor', 'Vendedor'),
        ('produtor', 'Produtor'),
    ]
    type = models.CharField(max_length=20, choices=TIPOS_USUARIO)
    confiavel = models.IntegerField()