from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import teacher


def index(request):
  teach = teacher.objects.all()

  return render(request, "MyApp1/index.html",{'content': teach})
  
def about(request):
   return render(
      request,
      "HelloDjangoApp/about.html",
      {
         'title' : "About HelloDjangoApp",
         'content' : "Example app page for Django."
      }
   )   

def main_view(request):
    return render(request, 'order/index.html',{})
    
    
    
    
    
    
    
   

# Create your views here.
