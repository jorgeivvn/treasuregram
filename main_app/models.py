from django.db import models
from django.contrib.auth.models import User

class Treasure(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(
    User,
    models.SET_NULL,
    blank=True,
    null=True,
)

def __str__(self):
    return self.name
