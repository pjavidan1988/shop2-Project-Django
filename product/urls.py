from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.all_product, name='product'),
]