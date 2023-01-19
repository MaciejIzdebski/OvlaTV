from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, mixins, exceptions
from rest_framework import permissions
from .permissions import IsOwner, IsPersonOwner, IsClientOwner
from . import serializers
from . import models
import inspect

class PersonViewSet(mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):

    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    permission_classes = [permissions.IsAuthenticated, IsPersonOwner]
    
    def get_object(self):
        try:
            person = self.request.user.client.person
        except:
            Http404

        # May raise a permission denied
        self.check_object_permissions(self.request, person)

        return person
        


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = [IsClientOwner]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        addresses = models.Address.objects.filter(person=self.request.user.client.person)
        return addresses


class TelephoneViewSet(viewsets.ModelViewSet):
    queryset = models.Telephone.objects.all()
    serializer_class = serializers.TelephoneSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        telephones = models.Telephone.objects.filter(person=self.request.user.client.person)
        return telephones

