#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .tables import ImageTable
from .tables import VideoTable
from .tables import AudioTable
from .models import Image
from .models import Video
from .models import Audio


def index(request):
    imageTable = ImageTable(Image.objects.all())
    videoTable = VideoTable(Video.objects.all())
    audioTable = AudioTable(Audio.objects.all())
    images_list = Image.objects.all()
    video_list = Video.objects.all()
    audio_list = Audio.objects.all()
    context = {
        'images_list': images_list,
        'video_list': video_list,
        'audio_list': audio_list,
        'imageTable': imageTable,
        'audioTable': audioTable,
        'videoTable': videoTable,
        }
    return render(request, 'gallery/index.html', context)


@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        first_name = jsonUser['first_name']
        last_name = jsonUser['last_name']
        password = jsonUser['password']
        email = jsonUser['email']

        user_model = User.objects.create_user(username=username,
                password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize('json', [user_model]))


@csrf_exempt
def add_user(request):
    return render(request, 'gallery/register.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = 'ok'
        else:
            message = \
                'Nombre de usuario o contrase\xc3\xb1a incorrectos'

    return JsonResponse({'message': message})


@csrf_exempt
def login_user(request):
    return render(request, 'gallery/login.html')


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'ok'})


def image_details(request, id):
    image = Image.objects.all().filter(id=id)
    url = Image.objects.get(id=id).url
    context = {'image': image, 'url': url}
    return render(request,
                  'gallery/tables/view_details_image_column.html',
                  context)


def video_details(request, id):
    video = Video.objects.all().filter(id=id)
    url = Video.objects.get(id=id).url
    context = {'video': video, 'url': url}
    return render(request,
                  'gallery/tables/view_details_video_column.html',
                  context)


def audio_details(request, id):
    audio = Audio.objects.all().filter(id=id)
    url = Audio.objects.get(id=id).url
    context = {'audio': audio, 'url': url}
    return render(request,
                  'gallery/tables/view_details_audio_column.html',
                  context)

@csrf_exempt
def add_image(request):
    if request.method == 'POST':
        newImage = Image(
            name=request.POST.get('name'),
            url = request.POST.get('url'),
            user = request.user,
            title = request.POST.get('title'),
            author = request.POST.get('author'),
            date = request.POST.get('date'),
            city = request.POST.get('city'),
            country = request.POST.get('country'),
            )
        newImage.save()
        return HttpResponse(serializers.serialize("json", [newImage]))