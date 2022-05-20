from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EventSerializer, EventCategorySerializer
from .models import Event, EventCategory

class EventCategoryList(generics.ListAPIView):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer

class UserEventList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = self.request.user
        category = request.query_params.get('category')
        pet_id = request.query_params.get('petId')

        queryset = Event.objects.filter(user=user)
        if category:
            queryset = queryset.filter(event_category__title = category)
        if pet_id:
            queryset = queryset.filter(pet_id = pet_id)

        
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

