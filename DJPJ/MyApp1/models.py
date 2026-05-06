from django.db import models

#class Courses (models.Model):
   #     Course = models.CharField(max_length=25)
     #   def __str__(self):
     #      return f"{self.Course} "

class teacher (models.Model):

   Name = models.CharField(max_length=25)
   # Course = models.ManyToManyField(Courses)
  
   

  #  def __str__(self):
   #     return f"{self.Name} "

class Area (models.Model):
       Name = models.ForeignKey(teacher, on_delete=models.CASCADE)
       Area = models.CharField(max_length=25)


       def __str__(self):
            return f"{self.Area} "



    
      
   

class subject (models.Model):
   Area = models.ForeignKey(Area, on_delete=models.CASCADE)
   subject = models.CharField(max_length=30)


