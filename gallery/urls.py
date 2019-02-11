from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^registerUser', views.add_user, name='registerUser'),
	url(r'^addUser/$', views.add_user_view, name='addUser'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^loginUser', views.login_user, name='loginUser'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^add/$', views.add_image, name='addImage'),
	url(r'^viewImage/$', views.image_view, name='viewImage'),
	url(r'^viewImages', views.viewImages, name='viewImages'),
    url(r'^addNewImage', views.add_new_image, name='addNewImage'),
	url(r'^isLogged/$', views.is_logged_view, name='isLogged'),

	path('imageDetails/<int:id>', views.image_details, name='imageDetails'),
	path('audioDetails/<int:id>', views.audio_details, name='audioDetails'),
	path('videoDetails/<int:id>', views.video_details, name='videoDetails'),	
]
