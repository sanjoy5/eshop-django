from django.contrib import admin
from .models import *

# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','company','update_at','status']



class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','status','note','create_at','update_at']
    readonly_fields = ['name','email','subject','message','ip']
    list_filter = ['status']


class SliderImageAdmin(admin.ModelAdmin):
    list_display = ['title','offer']

admin.site.register(Setting,SettingAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)
admin.site.register(SliderImage,SliderImageAdmin)
