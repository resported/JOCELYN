from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')


def NewUser(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'registration/registration.html', {'form': form})

    else:
        form = UserCreationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password1']
        new_user = User.objects.create(username=username, password=password)
        new_user.save()
        login(request, user=new_user)
        return redirect(index)


def LoginUser(request):
    form = UserCreationForm
    if request.method == 'POST':
        password = form.cleaned_data['password']
        username = form.cleaned_data['username']
        user = authenticate(username=username, password=password)
        login(user)
        redirect(index)

    else:
        return render(request, 'registration/login', {'form': form})
