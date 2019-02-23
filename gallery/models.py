

# Create your models here. editing gallery model
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.forms import ModelForm


class Image(models.Model):
    name= models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=140, default='')
    author = models.CharField(max_length=140, default='')
    date =  models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=140, default='')
    country = models.CharField(max_length=140, default='')
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5, blank=True)
    imageFile = models.ImageField(upload_to='staticfiles/images', null=True)

    def __str__(self):
        return 'Image: '+ self.name

class Categoria(models.Model):
    id = models.CharField(max_length=10,primary_key=id)
    descripcion = models.CharField(max_length=1000, null=False)

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'url', 'user', 'title', 'author', 'date', 'city', 'country', 'description', 'type', 'imageFile']


class Video(models.Model):
    name= models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=140, default='')
    author = models.CharField(max_length=140, default='')
    date =  models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=140, default='')
    country = models.CharField(max_length=140, default='')

    def __str__(self):
        return 'Video: '+ self.name

class Audio(models.Model):
    name= models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=140, default='')
    author = models.CharField(max_length=140, default='')
    date =  models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=140, default='')
    country = models.CharField(max_length=140, default='')

    def __str__(self):
        return 'Audio: '+ self.name

class ClipAudio(models.Model):
    name= models.CharField(max_length=200)
    secondStart= models.CharField(max_length=200)
    secondEnd= models.CharField(max_length=200)
    audioName= models.CharField(max_length=200)
    email= models.CharField(max_length=200,  null=True)


    def __str__(self):
        return 'ClipAudio: '+ self.name

class ClipVideo(models.Model):
    name= models.CharField(max_length=200)
    secondStart= models.CharField(max_length=200)
    secondEnd= models.CharField(max_length=200)    
    videoName= models.CharField(max_length=200)
    email= models.CharField(max_length=200,  null=True)

    def __str__(self):
        return 'ClipAudio: '+ self.name

class UserLogin(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='staticfiles/photo', null=True)
    city = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)

    def __str__(self):
        return 'UserLogin: '+ self.name
