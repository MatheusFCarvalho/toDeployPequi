from django.db import models
from my_user.models import User



class Pedido(models.Model):
    id = models.PositiveIntegerField(unique=True, primary_key=True)
    cliente = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f'{self.id} - {self.cliente}'