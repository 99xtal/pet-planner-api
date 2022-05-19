from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PetSerializer, BreedSerializer
from .models import Pet, Breed

class UserPetList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = self.request.user
        queryset = Pet.objects.filter(user=user)
        serializer = PetSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PetDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        pet = get_object_or_404(Pet, pk=pk)
        serializer = PetSerializer(pet)
        return Response(serializer.data)

    def put(self, request, pk):
        pet = get_object_or_404(Pet, pk=pk)
        serializer = PetSerializer(pet, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        pet = get_object_or_404(Pet, pk=pk)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BreedList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        queryset = Breed.objects.all()
        category = request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__category = category)
        serializer = BreedSerializer(queryset, many=True)
        return Response(serializer.data)