from django.shortcuts import render, redirect

# Create your views here.
from home.models import Setting
from .forms import userRegisterForm, userLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def user_register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['user_name'], email=data['email'],
                                     first_name=data['first_name'], last_name=data['last_name'],
                                     password=data['password_1'])
            return redirect('home:index')
    else:
        form = userRegisterForm()

    setting = Setting.objects.get(pk=1)

    context = {'setting': setting, 'form': form}
    return render(request, 'register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = userLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = authenticate(request, username=User.objects.get(email=data['user']), password=data['password'])
            except:
                user = authenticate(request, username=data['user'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('home:index')
            else:
                pass

    else:
        form = userLoginForm()

    setting = Setting.objects.get(pk=1)

    context = {'setting': setting, 'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('home:index')