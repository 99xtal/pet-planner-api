from rest_framework import permissions, generics
from .serializers import EventSerializer, EventCategorySerializer
from .models import Event, EventCategory


class EventCategoryList(generics.ListAPIView):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer


class UserEventList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        category = self.request.query_params.get("category")
        pet_id = self.request.query_params.get("petId")

        queryset = Event.objects.filter(user=user)
        if category:
            queryset = queryset.filter(event_category__title=category)
        if pet_id:
            queryset = queryset.filter(pet_id=pet_id)
        return queryset


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
