from rest_framework import serializers
from .models import Widget


class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = "__all__"
        depth = 1

    user_id = serializers.IntegerField(write_only=True)
    pet_id = serializers.IntegerField(write_only=True)
