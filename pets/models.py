from django.db import models
from authentication.models import User

# Create your models here.
class PetCategory(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.category}"

class Species(models.Model):
    binomial_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.binomial_name}"

class Breed(models.Model):
    category = models.ForeignKey(PetCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.category})"

class Pet(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    category = models.ForeignKey(PetCategory, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, default=None)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices= GENDER_CHOICES);
    weight = models.IntegerField(default=None)

    def __str__(self):
        return f"{self.name} ({self.category})"