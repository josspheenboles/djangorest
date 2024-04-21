from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello django 9month</h1>')
def book_list(request):
    books=Book.objects.all()
    return render(request,'book/list.html',context={'books':books})
def book_details(request,name):
    book=Book.objects.filter(name=name).first()
    return render(request,'book/details.html',context={'book':book})
    # return HttpResponse(f'<h1>book_list </h1>')
def book_add(request):
    # pythonbook=Book(name='python bible',latest_version=2)
    # pythonbook.save()
    # javabook=Book.objects.create(name='java bible')
    # return HttpResponse('<h1>book_add</h1>')
    return render(request,'book/add.html')
def book_update(request,id):
    return HttpResponse(f'<h1>book_update {id}</h1>')
def book_delete(request,id):
    return HttpResponse(f'<h1>book_delete {id}</h1>')