from django.db import models
from pets.models import PetCategory

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=64)
    pet_category = models.ForeignKey(PetCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Meal(models.Model):
    UNIT_CHOICES = [
        ('g', 'grams'),
        ('kg', 'kilograms'),
        ('cups', 'cups'),
        ('whole', 'whole')
    ]
    food = models.ForeignKey(Food, on_delete= models.CASCADE)
    amount= models.DecimalField(max_digits=10, decimal_places=2)
    amount_units = models.CharField(max_length=10, choices=UNIT_CHOICES)
    time = models.TimeField()

    def __str__(self):
        return f"{self.amount} {self.amount_units} {self.food}, {self.time}"