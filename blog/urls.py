from django.urls import path
from blog import views

urlpatterns = [
	path('',views.index,name='home'),
	path('<str:blog_slug>/',views.post, name='post'),

]