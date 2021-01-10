from django.contrib import admin
from django.urls import path
from . import views
from rest_framework import routers
#from .api import ProjectInfoViewSet

urlpatterns = [
    path('',views.index,name='index'),
]
