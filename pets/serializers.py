from rest_framework import serializers
from .models import Pet, Breed

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
        depth = 2

    user_id = serializers.IntegerField(write_only=True)
    category_id = serializers.IntegerField(write_only=True)
    breed_id = serializers.IntegerField(write_only=True)

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
        depth = 1