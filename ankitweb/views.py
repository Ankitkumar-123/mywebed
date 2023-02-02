from django.shortcuts import render,HttpResponse
from datetime import datetime
from ankitweb.models import contact
from django.contrib import messages
# Create your views here
def index(request):
    context={
        'variable':'zghdsvzhgvf variable',
        '':'xdfgdxgdx'
    }
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def Contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        Cont=contact(name=name,password=password,date=datetime.today())
        Cont.save()
        messages.success(request, 'form has been submitted')
    return render(request,'contact.html')

