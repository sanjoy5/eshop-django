from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent','status']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'status']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
