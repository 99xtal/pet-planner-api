from django.db import models
from pets.models import Pet
from authentication.models import User

# Create your models here.
class Widget(models.Model):
    WIDGET_CHOICES = [
        ("timeline", "timeline"),
        ("bio", "bio"),
        ("diet", "diet"),
        ("health", "health"),
    ]
    type = models.CharField(max_length=32, choices=WIDGET_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, default=None, blank=True, null=True
    )

    def __str__(self):
        if self.pet:
            str = f"{self.pet}'s {self.type} ({self.user})"
        else:
            str = f"{self.type} ({self.user})"
        return str
