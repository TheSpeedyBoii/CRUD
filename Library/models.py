from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Name')

    def __self__(self):
        return self.name
    
class Book(models.Model):
    id= models.AutoField(primary_key=True)
    title= models.CharField(max_length=100, verbose_name='Title')
    image= models.ImageField(upload_to='images/', verbose_name='Image', null=True)
    description= models.CharField(max_length=250, verbose_name='Description', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books", verbose_name="Category", null=True)

    def __str__(self):
        row = "Título: " + self.title + " - " + "Descripción: " + self.description
        return row

    def delete(self, using= None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()