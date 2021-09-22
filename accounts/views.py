from django.shortcuts import render

# Create your views here.
from home.models import Setting
from .forms import userRegisterForm
from django.contrib.auth.models import User


def user_register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['user_name'], email=data['email'],
                                     first_name=data['first_name'], last_name=data['last_name'],
                                     password=data['password_1'])

    else:
        form = userRegisterForm()
    setting = Setting.objects.get(pk=1)

    context = {'setting': setting, 'form':form }
    return render(request, 'accounts/register.html', context)