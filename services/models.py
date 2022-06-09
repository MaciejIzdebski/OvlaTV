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

class Offer (models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    nazwa = models.CharField(max_length=250)
    cena_za_mc = models.FloatField()

class  Contract (models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    offers = models.ManyToManyField(Offer)
    dateOfCreation = models.DateField(auto_now=True)
    dateOfSigning = models.DateField()
    # service = models
