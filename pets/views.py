from rest_framework import permissions, generics
from .serializers import PetSerializer, BreedSerializer
from .models import Pet, Breed

class UserPetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PetSerializer

    def get_queryset(self):
        user = self.request.user
        return Pet.objects.filter(user=user)

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class BreedList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BreedSerializer

    def get_queryset(self):
        queryset = Breed.objects.all()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__category = category)
        return queryset
