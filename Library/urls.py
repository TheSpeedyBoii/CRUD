from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('we', views.we, name="we"),
    path('books', views.books, name="books"),
    path('books/create', views.create, name="create"),
    path('books/edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)