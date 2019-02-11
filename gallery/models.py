

# Create your models here. editing gallery model
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

class Image(models.Model):
    name= models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5, blank=True)
    imageFile = models.ImageField(upload_to='images', null = True)
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)

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

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'url', 'description', 'type', 'imageFile']
