from django.contrib import admin
from .models import Pet, PetCategory, Breed, Species

# Register your models here.
admin.site.register([Pet, PetCategory, Breed, Species])
