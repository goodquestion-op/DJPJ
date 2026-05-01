from django.db import models

class teacher (models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class teacher_name (models.Model):
    BName = models.CharField(max_length=30)


