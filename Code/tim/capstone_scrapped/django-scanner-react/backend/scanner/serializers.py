from rest_framework import serializers
from .models import Scan

class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan
        fields = ('symbol',)