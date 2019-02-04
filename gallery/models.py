

# Create your models here. editing gallery model
from django.db import models


class Image(models.Model):
    name= models.CharField(max_length=200)
    url = models.CharField(max_length=1000)

    def __str__(self):
        return 'Image: '+ self.name

class Categoria(models.Model):
    id = models.IntegerField(max_length=5,primary_key=id)
    descripcion = models.CharField(max_length=50)

class Video(models.Model):
    name= models.CharField(max_length=200)
    url = models.CharField(max_length=1000)

    def __str__(self):
        return 'Video: '+ self.name

class Audio(models.Model):
    name= models.CharField(max_length=200)
    url = models.CharField(max_length=1000)

    def __str__(self):
        return 'Audio: '+ self.name