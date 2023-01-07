from django.contrib.auth.models import User, Group
from .models import Client, Person, Employee, Address, Telephone
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class TelephoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telephone
        fields = '__all__'

