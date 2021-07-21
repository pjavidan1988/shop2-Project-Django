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


def index(request):
    setting = Setting.objects.get(pk=1)

    context = {'setting': setting,}
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)

    context = {'setting': setting}
    return render(request, 'about.html', context)

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send and save data
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            # send and save data
            messages.success(request, "پیام شما با موفقیت ارسال شد")
            return HttpResponseRedirect('/contactus')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm
    context = {'setting': setting, 'form': form, 'category': category, }
    return render(request, 'contactus.html', context)

# def contactus(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # send and save data
#             data = ContactMessage()
#             data.name = form.cleaned_data['name']
#             data.email = form.cleaned_data['email']
#             data.phone = form.cleaned_data['phone']
#             data.subject = form.cleaned_data['subject']
#             data.message = form.cleaned_data['message']
#             data.ip = request.META.get('REMOTE_ADDR')
#             data.save()
#             # send and save data
#             messages.success(request, "پیام شما با موفقیت ارسال شد")
#             return HttpResponseRedirect('/contactus')
#
#     setting = Setting.objects.get(pk=1)
#     category = Category.objects.all()
#     form = ContactForm
#     context = {'setting': setting, 'form': form, 'category': category, }
#     return render(request, 'contact.html', context)