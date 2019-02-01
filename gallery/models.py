

# Create your models here. editing gallery model
from django.db import models


class Image(models.Model):
    name= models.CharField(max_length=200)
    url = models.CharField(max_length=1000)

    def __str__(self):
        return 'Image: '+ self.name
