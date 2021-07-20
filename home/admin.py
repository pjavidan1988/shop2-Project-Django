from django.contrib import admin

# Register your models here.
from home.models import Setting, brandImages

class SettingbarandImageInline(admin.TabularInline):
    model = brandImages
    extra = 5

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']
    inlines = [SettingbarandImageInline]


admin.site.register(Setting,SettingAdmin)