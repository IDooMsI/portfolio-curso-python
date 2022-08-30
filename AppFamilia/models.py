from operator import mod
from statistics import mode
from django.db import models

class Familiar(models.Model):
    parentesco = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()