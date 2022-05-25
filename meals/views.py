from rest_framework import permissions, generics
from .serializers import FoodSerializer, MealSerializer
from .models import Food, Meal


class MealList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MealSerializer

    def get_queryset(self):
        queryset = Meal.objects.all()
        pet_id = self.request.query_params.get("petId")

        if pet_id:
            queryset = queryset.filter(pet_id=pet_id)
        return queryset


class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class FoodList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FoodSerializer

    def get_queryset(self):
        queryset = Food.objects.all()
        categoryId = self.request.query_params.get("categoryId")

        if categoryId:
            queryset = queryset.filter(pet_category__id=categoryId)
        return queryset


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
