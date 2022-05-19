from rest_framework import serializers
from .models import Meal, Food

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model= Meal
        fields = '__all__'
        depth = 1

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'