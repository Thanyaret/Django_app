from django.contrib import admin
from .models import UserProfile,maid
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','address')

class maidAdmin(admin.ModelAdmin):
    list_display = ('id','name','detail')

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(maid,maidAdmin)
