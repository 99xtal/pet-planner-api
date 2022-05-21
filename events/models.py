from django.db import models
from authentication.models import User
from pets.models import Pet


class EventCategory(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Event(models.Model):
    event_category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField(default="00:00:00", blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
