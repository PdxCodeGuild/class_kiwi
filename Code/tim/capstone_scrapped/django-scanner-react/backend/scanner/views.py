from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ScanSerializer
from .models import Scan

# Create your views here.
class ScanView(viewsets.ModelViewSet):
    serializer_class = ScanSerializer
    queryset = Scan.objects.all()