from rest_framework import serializers
from .models import Event, EventCategory

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        depth = 1

    event_category_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)
    pet_id = serializers.IntegerField(write_only=True)

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = '__all__'
