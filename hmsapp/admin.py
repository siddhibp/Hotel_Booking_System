from django.contrib import admin
from hmsapp.models import abc
# Register your models here.

class abcName(admin.ModelAdmin):
    list_display =['id','name','price','details','category','image']

admin.site.register(abc,abcName)