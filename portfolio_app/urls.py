from django.contrib import admin
from django.urls import path
from . import views
from rest_framework import routers
#from .api import ProjectInfoViewSet
# CAUSING ERROR

urlpatterns = [
    path('',views.index,name='index'),
]
