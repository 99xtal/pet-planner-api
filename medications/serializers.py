from rest_framework import serializers
from .models import Medicine, Medication

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

    pet_category_id = serializers.IntegerField(write_only = True)
    
class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'
        depth = 1

    medicine_id = serializers.IntegerField(write_only= True)
    pet_id = serializers.IntegerField(write_only = True)