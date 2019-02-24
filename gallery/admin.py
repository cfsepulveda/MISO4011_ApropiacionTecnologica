from django.contrib import admin

# Register your models here. Added gallery model
from .models import Image
from .models import Video
from .models import Audio
from .models import Categoria
from .models import ClipAudio
from .models import ClipVideo
from .models import UserLogin
from .models import  MediaType


admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Categoria)
admin.site.register(ClipAudio)
admin.site.register(ClipVideo)
admin.site.register(UserLogin)
admin.site.register(MediaType)