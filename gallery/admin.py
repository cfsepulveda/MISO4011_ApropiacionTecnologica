from django.contrib import admin

# Register your models here. Added gallery model
from .models import Image
from .models import Video
from .models import Audio
from .models import Categoria

admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Categoria)