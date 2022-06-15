from http import client
from re import T
from statistics import mode
from sys import maxsize
from tkinter import CASCADE
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from pyparsing import null_debug_action

# Create your models here.
class Client(models.Model):
    email = models.EmailField(null=True)

    def __str__(self) -> str:
        return self.pk

    @property
    def pesel(self):
        return self.person.pesel

class Person(models.Model):
    GENDER_TYPES = [
        ('F', 'Kobieta'),
        ('M', 'Mężczyzna')
    ]
    pesel = models.CharField(max_length=11, null=True)
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length=100, default='')
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_TYPES, null=True)
    id_card_number = models.CharField(max_length=9, null=True)
    id_card_scan = models.ImageField(null=True)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.pesel


class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=10)
    apartmentNumber = models.CharField(max_length=5)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name_plural = 'addresses'

    def __str__(self) -> str:
        return self.person.pesel

class Employee(models.Model):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    hire_date = models.DateField(auto_now=True)
    fire_date = models.DateField(null=True)
    

class Telephone(models.Model):
    telephone = models.CharField(max_length=11) # +3 cyfry kierunkowego
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.person.pesel