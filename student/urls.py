from django.contrib import admin
from django.urls import path, include

from student import views

urlpatterns = [

  path('score', views.score, name='score'),
  path('', views.landing, name='landing'),



]