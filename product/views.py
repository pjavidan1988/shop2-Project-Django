from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def all_product(request):
    return HttpResponse("my product page")
