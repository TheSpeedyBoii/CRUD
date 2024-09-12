from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'pages/index.html')

def we(request):
    return render(request, 'pages/we.html')

def books(request):
    return render(request, 'books/index.html')

def create(request):
    return render(request, 'books/create.html')

def edit(request):
    return render(request, 'books/edit.html')