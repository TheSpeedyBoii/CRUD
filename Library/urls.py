from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('we', views.we, name="we"),
    path('books', views.books, name="books"),
    path('books/create', views.create, name="create"),
    path('books/edit', views.edit, name="edit")
]