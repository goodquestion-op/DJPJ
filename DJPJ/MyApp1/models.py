from django.db import models

class teacher (models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class teacher_name (models.Model):
    TName = models.CharField(max_length=20)

#class courseArea (models.Model):
#    Teacher = models.ManyToManyField(teacher) 

# Create your models here.
