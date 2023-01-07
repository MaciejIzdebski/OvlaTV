from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from . import serializers
from . import models

class ServiceLocationViewSet(viewsets.ModelViewSet):
    queryset = models.ServiceLocation.objects.all()
    serializer_class = serializers.ServiceLocationSerializer
    permission_classes = [permissions.AllowAny]

class OfferViewSet(viewsets.ModelViewSet):
    queryset = models.Offer.objects.all()
    serializer_class = serializers.OfferSerializer
    permission_classes = [permissions.AllowAny]

class ContractViewSet(viewsets.ModelViewSet):
    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractSerializer
    permission_classes = [permissions.AllowAny]

class DebtViewSet(viewsets.ModelViewSet):
    queryset = models.Debt.objects.all()
    serializer_class = serializers.DebtSerializer
    permission_classes = [permissions.AllowAny]