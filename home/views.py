from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    uni = "meybod"
    dept = "computer Engineering"
    context = {'uni':uni, 'dept':dept}
    return render(request,'index.html', context)

