from django.shortcuts import render, redirect

# Create your views here.
from home.models import Setting
from .models import Profile
from .forms import userRegisterForm, userLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['user_name'], email=data['email'],
                                     first_name=data['first_name'], last_name=data['last_name'],
                                     password=data['password_1'])
            user.save()
            messages.success(request, 'ثبت نام با موفقیت انجام شد لطفا وارد شوید', 'success')
            return redirect('accounts:login')
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
                messages.success(request,'کاربر عزیز خوش آمدید','success' )
                return redirect('home:index')
            else:
                messages.warning(request,'کاربر عزیز نام کاربری یا پسورد اشتباه است','danger' )

    else:
        form = userLoginForm()

    setting = Setting.objects.get(pk=1)

    context = {'setting': setting, 'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید','success')
    return redirect('home:index')


def user_profile(request):
    profile = Profile.objects.get(user_id=request.user.id)

    setting = Setting.objects.get(pk=1)

    context = {'setting': setting, 'profile':profile}
    return render(request, 'profile.html', context)