from http import client
from re import T
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

# Create your models here.

class Person(models.Model):
    GENDER_TYPES = [
        ('F', 'Kobieta'),
        ('M', 'Męszczyzna')
    ]
    pesel = models.TextField(max_length=11, null=True)
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length=100, default='')
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_TYPES, null=True)


class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=10)
    apartmentNumber = models.CharField(max_length=5)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name_plural = 'addresses'

class Employee(models.Model):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    hire_date = models.DateField(auto_now=True)
    fire_date = models.DateField(null=True)
    
class Client(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class Telephone(models.Model):
    telephone = models.CharField(max_length=11) # +3 cyfry kierunkowego
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)