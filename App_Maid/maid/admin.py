from django.contrib import admin
from .models import User,maid
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('photo','name','address')

class maidAdmin(admin.ModelAdmin):
    list_display = ('photo','name','detail')

admin.site.register(User,UserAdmin)
admin.site.register(maid,maidAdmin)