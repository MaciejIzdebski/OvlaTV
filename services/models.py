from enum import auto
from http import client
from multiprocessing.connection import Client
from os import truncate
from pickle import TRUE
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from users.models import Client

class ServiceLocation (models.Model):
    ulica = models.CharField(max_length=75)
    numer_domu = models.CharField(max_length=10)
    max_przepustowosc = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.ulica

class Offer (models.Model):
    nazwa = models.CharField(max_length=250)
    cena_za_mc = models.FloatField()
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.nazwa

class  Contract (models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    offers = models.ManyToManyField(Offer)
    dateOfCreation = models.DateField(auto_now=True)
    dateOfSigning = models.DateField()

    def __str__(self):
        return str(self.pk) + '/' + str(self.dateOfSigning)

class Debt (models.Model):
    receivable = models.IntegerField()
    date = models.DateField()