from django.contrib import admin
from .models import Medicine, Medication

# Register your models here.
admin.site.register([Medicine, Medication])