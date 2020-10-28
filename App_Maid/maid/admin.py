from django.contrib import admin
from .models import UserProfile,maid,statusmaid
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','address')

class maidAdmin(admin.ModelAdmin):
    list_display = ('id','name','detail')

class statusmaidAdmin(admin.ModelAdmin):
    list_display = ('id','maid_name','date','user','status')

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(maid,maidAdmin)
admin.site.register(statusmaid,statusmaidAdmin)
