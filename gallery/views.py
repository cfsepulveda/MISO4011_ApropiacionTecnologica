from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from .models import Video
from .models import Audio

def index(request):
	images_list = Image.objects.all()
	video_list = Video.objects.all()
	audio_list = Audio.objects.all()
	context = {'images_list': images_list,
			   'video_list':video_list,
			   'audio_list': audio_list}
	return render(request, 'gallery/index.html', context)



