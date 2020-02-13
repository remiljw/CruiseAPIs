from rest_framework import serializers
from .models import *

class ExcursionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excursion
        fields= '__all__'

