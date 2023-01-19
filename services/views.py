from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions, mixins
from . import serializers
from . import models

class ServiceLocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.ServiceLocation.objects.all()
    serializer_class = serializers.ServiceLocationSerializer
    permission_classes = [permissions.AllowAny]

class OfferViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Offer.objects.all()
    serializer_class = serializers.OfferSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        offers = models.Offer.objects.filter(pk=1)
        return offers   

class ContractViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        contracts = models.Contract.objects.filter(pk=1)
        return contracts  

class DebtViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Debt.objects.all()
    serializer_class = serializers.DebtSerializer
    permission_classes = [permissions.AllowAny]
