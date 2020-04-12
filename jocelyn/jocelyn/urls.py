"""jocelyn URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', NewUser, name='registration'),
    path('<username>', current_user, name='current_user'),
]
