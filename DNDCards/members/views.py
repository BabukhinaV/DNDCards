from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from catalog.models import Player
from .forms import RegisterUserForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('home')
            else:
                return redirect('home')
        else:
            messages.success(request, ("Ошибка авторизации"))
            return redirect('login')
    else:
        return render(request, 'authentification/login.html', {})


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            player = Player(name = '', level = 1, pclass=None, race = None, exp = 0, history = None, user = user, img = 'images/user.png')
            player.save()
            login(request, user)
            messages.success(request, ("Вы зарегистрированы."))
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'authentification/register_user.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, ("Выход из учетной записи"))
    return redirect('login')
