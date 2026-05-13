from ast import Return
from urllib.request import Request
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from .models import teacher
from .forms import InputForm,Mydropdownform,CommentForm
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from pypdf import PdfWriter, PdfReader 
from reportlab.pdfgen import canvas 
from reportlab.platypus import Paragraph,Image,Table
from django.http import FileResponse 
from django.contrib.staticfiles.storage import staticfiles_storage 
from io import BytesIO
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login




def index(request):
  teach = teacher.objects.all()
  form = Mydropdownform()
  info_extra = CommentForm
  return render(request, "MyApp1/index.html",{'content': teach,'form': form,'info_extra':info_extra})


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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #login(request, form.save())
            return redirect( "MyApp1/index.html")
    else:
        form = UserCreationForm()
    return render(request, "MyApp1/input.html", { 'form':form })

def login(request):
    if request.method == "POST":
         form = AuthenticationForm(data = request.POST) #special kind of form beacue sign in
         if form.is_valid():
             #login(request, form.get_user())
             return redirect( "index")
    else:
        form = AuthenticationForm
    return render(request, "MyApp1/login.html",{'form':form}) 




def report(request):
    pdf_file= staticfiles_storage.path("PDF_OUTPUT.pdf")

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
        lines.append((teach.Name))

    table = Table(lines)

    table.wrapOn(p,10,10)

    table.drawOn(p,11,700)
        
    p.showPage()
    p.save()   

    buffer.seek(0)
    return buffer


       
    
    
   

# Create your views here.
