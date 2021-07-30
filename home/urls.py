from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Videos, name="Videos"),
    path('Whenplay/videos<int:Video_id>in-shareits',
         views.Whenplay, name="Whenplay"),
    path('<str:Username>.html', views.channel, name="channel"),
    path('search', views.search, name="search"),
    path('signup', views.signup, name="signup"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]
