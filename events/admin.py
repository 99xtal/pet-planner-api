from django.contrib import admin
from .models import Event, EventCategory

# Register your models here.
admin.site.register([Event, EventCategory])