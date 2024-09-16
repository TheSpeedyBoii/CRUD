from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Category
from .forms import BookForm, CategoryForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    return render(request, 'pages/index.html')

def we(request):
    return render(request, 'pages/we.html')

@login_required
def books(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def create(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request, "books/create.html", {"form": form})

def edit(request, id):
    book_ed = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book_ed)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('books')
    return render(request, "books/edit.html", {"form": form})

def delete(request, id):
    libro_delete = Book.objects.get(id=id)
    libro_delete.delete()
    return redirect('books')

@login_required
def category(request):
    category = Category.objects.all()
    return render(request, 'category/index.html', {'category': category})

@login_required
def create_category(request):
    form = CategoryForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('category')
    return render(request, 'category/edit.html', {"form": form})

@login_required
def delete_category(request, id):
    cat_delete = Category.objects.get(id=id)
    cat_delete.delete()
    return redirect('category')