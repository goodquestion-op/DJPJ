from email.policy import default
from django.contrib.auth.models import User
from django.db import models

class CustomUser(User):
    phone_number = models.CharField(max_length=15, blank=True)

class Areas (models.Model):
        Area = models.CharField(max_length=25)
        def __str__(self):
           return f"{self.Area} "

class teacher (models.Model):

   Name = models.CharField(max_length=25)
   Area = models.ManyToManyField(Areas)
   def __str__(self):
        return f"{self.Name} "
         
class Courses (models.Model):
       #Area = models.ForeignKey(Areas, on_delete=models.CASCADE)
       Course = models.CharField(max_length=100)
       
       def __str__(self):
            return f"{self.Course} "
    
class Units (models.Model):
   #Course = models.ForeignKey(Courses, on_delete=models.CASCADE) 
   Unit = models.CharField(max_length=30)
   def __str__(self):
        return  f"{self.Unit} "



