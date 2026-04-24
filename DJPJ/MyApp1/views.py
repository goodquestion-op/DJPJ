from django.shortcuts import render, redirect
from .models import teacher
from .forms import InputForm
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import Mydropdownform



def index(request):
  teach = teacher.objects.all()
  form = Mydropdownform()

  return render(request, "MyApp1/index.html",{'content': teach)




 
#def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
 #   response = HttpResponse(content_type='application/pdf')
 #   response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

#    # Create the PDF object, using the response object as its "file."
 #   p = canvas.Canvas(response)
#
 #   # Draw things on the PDF. Here's where the PDF generation happens.
 #   # See the ReportLab documentation for the full list of functionality.
 #   p.drawString(100, 100, "Hello world.")
#
 #   # Close the PDF object cleanly, and we're done.
 #   p.showPage()
 #   p.save()
   # return response

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
