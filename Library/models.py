from django.db import models

# Create your models here.

class Book(models.Model):
    id= models.AutoField(primary_key=True)
    title= models.CharField(max_length=100, verbose_name='Title')
    image= models.ImageField(upload_to='images/', verbose_name='Image', null=True)
    description= models.CharField(max_length=250, verbose_name='Description', null=True)