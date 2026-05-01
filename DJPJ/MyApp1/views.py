from django.shortcuts import render, redirect
from .models import teacher
from .forms import InputForm
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import Mydropdownform

from pypdf import PdfWriter, PdfReader 
from reportlab.pdfgen import canvas 
from reportlab.platypus import Paragraph,Image,Table
from django.http import FileResponse 
from django.contrib.staticfiles.storage import staticfiles_storage 
from io import BytesIO




def index(request):
  teach = teacher.objects.all()
  form = Mydropdownform()
  return render(request, "MyApp1/index.html",{'content': teach,'form': form})


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
def report(request):
    pdf_file= staticfiles_storage.path("digitalSoultions.pdf")

    try:
        merger = PdfWriter()

        input1 = PdfReader(generate_pdf())
        input2 = PdfReader(pdf_file, "rb")

        merger.append(input1)
        merger.append(input2)

        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)

        response = FileResponse(buffer, as_attachment=True, filename="attachment.pdf")

    except FileNotFoundError:
        response = FileResponse(generate_pdf(), as_attachment=True, filename="noAttachment.pdf")
    return response
def generate_pdf():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    lines = [('Name:', 'Teaching Area:')]

    teachers = teacher.objects.all()
    
    for teach in teachers:
        lines.append((teach.Name, teach.Area))

    table = Table(lines)

    table.wrapOn(p,10,10)

    table.drawOn(p,11,700)
        
    p.showPage()
    p.save()   

    buffer.seek(0)
    return buffer
    
    
    
   

# Create your views here.
