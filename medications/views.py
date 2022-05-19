from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MedicineSerializer, MedicationSerializer
from .models import Medicine, Medication

class MedicationList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class MedicationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class MedicineList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        category = request.query_params.get('category')
        if category:
            queryset = Medicine.objects.filter(pet_category__category = category)
        else:
            queryset = Medicine.objects.all()
        serializer = MedicineSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MedicineSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MedicineDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer