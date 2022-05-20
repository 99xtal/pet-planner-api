from django.shortcuts import get_object_or_404
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FoodSerializer, MealSerializer
from .models import Food, Meal

class MealList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        pet_id = request.query_params.get('petId')
        if pet_id:
            queryset = Meal.objects.filter(pet_id = pet_id)
        else:
            queryset = Meal.objects.all()
        serializer = MealSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MealSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class FoodList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        category = request.query_params.get('category')
        if category:
            queryset = Food.objects.filter(pet_category__category = category)
        else:
            queryset = Food.objects.all()
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Food.objects.all()
    serializer_class = FoodSerializer