from rest_framework import permissions, generics
from .serializers import MedicineSerializer, MedicationSerializer
from .models import Medicine, Medication


class MedicationList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MedicationSerializer

    def get_queryset(self):
        queryset = Medication.objects.all()
        pet_id = self.request.query_params.get("petId")
        if pet_id:
            queryset = queryset.filter(pet_id=pet_id)
        return queryset


class MedicationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class MedicineList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MedicineSerializer

    def get_queryset(self):
        queryset = Medicine.objects.all()
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(pet_category__category=category)
        return queryset


class MedicineDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
