from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone','postal_code','city']

admin.site.register(Profile,ProfileAdmin)

