from rest_framework import serializers
from .models import Meal, Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
        depth = 1

    pet_category_id = serializers.IntegerField(write_only=True)
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model= Meal
        fields = '__all__'
        depth = 1

    food_id = serializers.IntegerField(write_only=True)
    pet_id = serializers.IntegerField(write_only = True)
    
