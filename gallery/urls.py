from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('addUser/', views.add_user_view, name='addUser'),
	path('registerUser/', views.add_user, name='registerUser'),
    path('add/', views.add_image, name='addImage'),
]
