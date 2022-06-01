from statistics import mode
from django.db import models

# Create your models here.

class Person(models.Model):
    GENDER_TYPES = [
        ('F', 'Kobieta'),
        ('M', 'Męszczyzna')
    ]
    pesel = models.TextField(max_length=11)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length='1', choices=GENDER_TYPES)

