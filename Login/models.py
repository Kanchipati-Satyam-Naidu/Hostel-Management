from django.db import models as m
from django.contrib.auth.models import AbstractUser
from Hostel.models import *

# Create your models here.

class User(AbstractUser):
    us=[
        ("User","User"),
        ("Guest","Guest"),
        ("Admin","Admin"),
    ]
    first_name=m.CharField(max_length=30)
    last_name=m.CharField(max_length=30)
    username=m.CharField(max_length=50,unique=True)
    email=m.CharField(max_length=40)
    mobile=m.CharField(max_length=10)
    role_type=m.CharField(max_length=20,choices=us,default="User")
    room_no=m.CharField(max_length=10)

class Feedback(m.Model):
    email=m.CharField(max_length=40)
    description=m.CharField(max_length=200)
    rating=m.IntegerField()