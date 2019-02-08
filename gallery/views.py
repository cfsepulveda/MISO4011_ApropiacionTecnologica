from django.contrib.auth.models import User
from django.core import serializers
from django.core.serializers import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from .models import Video
from .models import Audio
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image, ImageForm


def index(request):
	images_list = Image.objects.all()
	video_list = Video.objects.all()
	audio_list = Audio.objects.all()
	context = {'images_list': images_list,
			   'video_list':video_list,
			   'audio_list': audio_list}
	return render(request, 'gallery/index.html', context)

def add_user_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        first_name = jsonUser['first_name']
        last_name = jsonUser['last_name']
        password = jsonUser['password']
        email = jsonUser['email']

        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))


def add_image(request):
    if request.method == 'POST':  # Si se enviaron datos para almacenar
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('images:index'))
    else:  # No se enviaron datos para almacenar, se muestra el formulario
        form = ImageForm()

    return render(request, 'gallery/image_form.html', {'form': form})


def add_user(request):
    return render(request, "gallery/register.html")


