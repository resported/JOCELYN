
from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [
    #include()
    ######################## MAIN #######################
    path('', index, name='index'),
]