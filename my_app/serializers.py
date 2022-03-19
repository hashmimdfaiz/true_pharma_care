from rest_framework import serializers
from .models import Doctor,Provider


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields = '__all__'

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Provider
        fields = '__all__'