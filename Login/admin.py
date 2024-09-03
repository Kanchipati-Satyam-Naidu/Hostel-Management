from django.contrib import admin
from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display=["username","email","mobile","role_type"]

class AdminViewFeedback(admin.ModelAdmin):
    list_display=["email","description","rating"]

admin.site.register(User,UserAdmin)
admin.site.register(Feedback,AdminViewFeedback)