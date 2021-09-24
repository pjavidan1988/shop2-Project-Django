import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation

# from home.models import Setting, ContactForm, ContactMessage

# Create your views here.
from home.models import Setting, ContactForm, ContactMessage
from product.models import Category, Product
from django.core.mail import EmailMessage


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, }
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'about.html', context)


def contactus(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['msg']
        body =  ' موضوع :' + '\n' + subject +  '\n' + '\n'+' نام :'  + '\n' + name + '\n' + '\n' + '\n'+ ' متن پیام :'  + '\n' + msg +  '\n' + '\n' + '\n' + 'From: ' + email
        form = EmailMessage(
            'پیام از طرف سایت',
            body,
            'message',
            ('p.javidan1988@gmail.com',)
        )
        form.send(fail_silently=True)
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'contactus.html', context)
