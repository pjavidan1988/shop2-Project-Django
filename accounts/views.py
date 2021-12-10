import ghasedak
from django.shortcuts import render, redirect

# Create your views here.
from home.models import Setting
from .models import Profile
from .forms import userRegisterForm, userLoginForm, userUpdateForm, profileUpdateForm, phoneForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from random import randint


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

@login_required(login_url='accounts:login')
def user_profile(request):
    profile = Profile.objects.get(user_id=request.user.id)

    setting = Setting.objects.get(pk=1)

    context = {'setting': setting, 'profile':profile}
    return render(request, 'profile.html', context)

@login_required(login_url='accounts:login')
def user_update(request):
    if request.method == 'POST':
        user_form = userUpdateForm(request.POST, instance=request.user)
        profile_form = profileUpdateForm(request.POST, instance=request.user.profile)
        if user_form and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'تغییرات با موفقیت انجام شد', 'success')
            return redirect('accounts:profile')
    else:
        user_form = userUpdateForm(instance=request.user)
        profile_form = profileUpdateForm(instance=request.user.profile)

    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'user_form':user_form, 'profile_form':profile_form}
    return render(request, 'update.html', context)

@login_required(login_url='accounts:login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'پسورد با موفقیت تغییر یافت', 'success')
            return redirect('accounts:profile')
        else:
            messages.warning(request,'کاربر عزیز پسورد وارد شده اشتباه است','danger' )
            return redirect('accounts:change_password')
    else:
        form = PasswordChangeForm(request.user)
        setting = Setting.objects.get(pk=1)
        context = {'setting': setting,'form':form}
    return render(request, 'change_password.html', context)


def phone(request):
    if request.method == 'POST':
        form = phoneForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            phone = data['phone']
            random_code = randint(100,1000)
            sms = ghasedak.Ghasedak("")
            sms.send({'message': random_code, 'receptor': phone, 'linenumber': "10008566"})
            return redirect()
    else:
        form = phoneForm()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'form':form}
    return render(request, 'phone.html', context)