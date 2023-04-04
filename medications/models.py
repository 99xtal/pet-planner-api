from django.db import models
from pets.models import PetCategory, Pet

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=64)
    pet_category = models.ForeignKey(PetCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.pet_category})"


class Medication(models.Model):
    UNIT_CHOICES = [("pills", "pills"), ("ccs", "ccs"), ("drops", "drops")]
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_units = models.CharField(max_length=10, choices=UNIT_CHOICES)
    time = models.TimeField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} {self.amount_units} {self.medicine}, {self.time}"
