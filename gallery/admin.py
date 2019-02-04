from django.contrib import admin

# Register your models here. Added gallery model
from .models import Image

admin.site.register(Image)
