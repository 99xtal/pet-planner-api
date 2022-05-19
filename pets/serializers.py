from rest_framework import serializers
from .models import Pet, PetCategory, Species, Breed

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'user', 'name', 'category', 'breed', 'birthday', 'gender', 'weight']

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'