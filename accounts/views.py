from django.shortcuts import render

# Create your views here.
from home.models import Setting


def user_register(request):
    setting = Setting.objects.get(pk=1)

    context = {'setting': setting, }
    return render(request,'accounts/register.html', context)