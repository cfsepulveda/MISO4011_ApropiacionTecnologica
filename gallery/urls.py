from django.urls import path

from gallery.views import CategoriaList
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('categorias', CategoriaList.as_view(), name='categorias_list'),
]
