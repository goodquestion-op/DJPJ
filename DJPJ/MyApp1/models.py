from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

class teacher (models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)
class Car(models.Model):
    name = models.CharField(max_length=80)
    country = models.CharField(max_length=100)

    def __str__(self):

        return str(self.name)

class Model(models.Model):
     name = models.CharField(max_length=50)
     can = models.ForeignKey(Car, on_delete=models.CASCADE)

     def __str__(self):

        return f"{self.car}-{self.name}"

class Order(models.Model):

    

# Create your models here.
