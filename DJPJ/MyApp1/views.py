from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import InputForm
from django.shortcuts import render, redirect
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

def input_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = InputForm()
    return render(request, "MyApp1/input.html", {"form": form})
    
    
    
    
    
    
    
   

# Create your views here.
