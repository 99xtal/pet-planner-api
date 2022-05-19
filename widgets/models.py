from django.db import models
from pets.models import Pet
from authentication.models import User

# Create your models here.
class Widget(models.Model):
    WIDGET_CHOICES = [
        ('timeline', 'timeline'),
        ('bio','bio'),
        ('diet','diet'),
        ('medications', 'medications')
    ]
    type = models.CharField(max_length=32, choices=WIDGET_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, default=None, blank=True, null=True)
