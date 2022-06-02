from rest_framework import serializers
from .models import Dog


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "owner", "coat", "gender", "description", "date_entered")
        model = Dog
