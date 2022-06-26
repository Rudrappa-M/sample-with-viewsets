from dataclasses import field
import imp
from .models import product
from rest_framework import serializers

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'