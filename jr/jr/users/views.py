from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .models import User
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'user_example/index.html')

def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        password = form.cleaned_data['password']
        username = form.cleaned_data['username']
        user = authenticate(username=username, password=password)
        login(user)
        redirect(index)

    else:
        return render(request, 'registration.html')








