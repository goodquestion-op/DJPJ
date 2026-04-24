from unittest.util import _MAX_LENGTH
from django.db import models

class teacher (models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class testing (models.Model):
    test = models.CharField(max_length=30)
#class courseArea (models.Model):
#    Teacher = models.ManyToManyField(teacher) 

# Create your models here.
