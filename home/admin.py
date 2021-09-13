from django.contrib import admin

# Register your models here.
from home.models import Setting, brandImages, ContactMessage


class SettingbarandImageInline(admin.TabularInline):
    model = brandImages
    extra = 5

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']
    inlines = [SettingbarandImageInline]

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'update_at', 'status']
    readonly_fields = ('name', 'subject', 'email', 'message', 'ip')

admin.site.register(Setting,SettingAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)