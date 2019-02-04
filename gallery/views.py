from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

from django.views.generic import ListView
from gallery.models import Categoria

def index(request):
	images_list = Image.objects.all()
	context = {'images_list': images_list}
	return render(request, 'gallery/index.html', context)

class CategoriaList(ListView):
	model = Categoria
	template_name = 'templates/Categorias/categoria_list.html'