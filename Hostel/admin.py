from django.contrib import admin
from .models import *

# Register your models here.

class Tenants_View(admin.ModelAdmin):
    list_display=["Name","profession","year","mobile","aadhar","stay_type","room_type","room_no","DOJ","fee","payment_status"]

class Hostel_Admin_View(admin.ModelAdmin):
    list_display=["floor_no","room_no","room_type","room_status","total_no_of_beds","no_of_beds_ava","fee"]

class Problem_View(admin.ModelAdmin):
    list_display=["username","email","room_no","issue"]

admin.site.register(Tenants,Tenants_View)
admin.site.register(Hostel,Hostel_Admin_View)
admin.site.register(Problem,Problem_View)