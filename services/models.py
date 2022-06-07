from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

class ServiceLocation (models.Model):
    ulica = models.CharField(max_length=75);
    numer_domu = models.CharField(max_length=10);
    max_przepustowosc = models.DecimalField;


