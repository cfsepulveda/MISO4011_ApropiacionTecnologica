

# Create your models here. editing gallery model
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Image(models.Model):
    name= models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
	title = models.CharField(max_length=140, default='')
    author = models.CharField(max_length=140, default='')
    date =  models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=140, default='')
    country = models.CharField(max_length=140, default='')  

    def __str__(self):
        return 'Image: '+ self.name


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

