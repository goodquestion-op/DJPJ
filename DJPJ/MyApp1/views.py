from django.shortcuts import render, redirect
from .models import teacher
from .forms import InputForm
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import Mydropdownform



def index(request):
  teach = teacher.objects.all()

  return render(request, "MyApp1/index.html",{'content': teach})

def index(request):
    form = Mydropdownform()
    return render(request, "MyApp1/index.html", {'form': form})


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
