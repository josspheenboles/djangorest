from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello django 9month</h1>')
def book_list(request):
    return HttpResponse('<h1>book_list</h1>')