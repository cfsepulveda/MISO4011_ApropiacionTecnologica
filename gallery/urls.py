from django.conf.urls import url
from django.urls import path

from gallery.views import CategoriaList
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('categorias', CategoriaList.as_view(), name='categorias_list'),
	path('addUser/', views.add_user_view, name='addUser'),
	path('registerUser/', views.add_user, name='registerUser'),
	url(r'^$', views.index, name='index'),
	url(r'^registerUser', views.add_user, name='registerUser'),
	url(r'^addUser/$', views.add_user_view, name='addUser'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^loginUser/$', views.login_user, name='loginUser'),
	url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^add/$', views.add_image, name='addImage'),
]
