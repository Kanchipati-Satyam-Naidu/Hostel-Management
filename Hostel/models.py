from django.db import models as m

# Create your models here.

class Hostel(m.Model):
    rt=[
        ("AC 2-Sharing","AC 2-Sharing"),
        ("AC 3-Sharing","AC 3-Sharing"),
        ("Non AC 2-Sharing","Non AC 2-Sharing"),
        ("Non AC 3-Sharing","Non AC 3-Sharing"),
    ]
    
    av=[
        ("Full/Unavailable","Full/Unavailable"),
        ("Available","Available"),
    ]
    floor_no=m.IntegerField()
    room_no=m.CharField(max_length=10,primary_key=True)
    room_type=m.CharField(max_length=30,choices=rt)
    room_status=m.CharField(max_length=25,choices=av)
    total_no_of_beds=m.IntegerField()
    no_of_beds_ava=m.IntegerField()
    fee=m.IntegerField()

class Tenants(m.Model):
    p=[
        ("Student","Student"),
        ("Employee","Employee"),
        ("Other","Other"),
    ]
    rt=[
        ("AC 2-Sharing","AC 2-Sharing"),
        ("AC 3-Sharing","AC 3-Sharing"),
        ("Non AC 2-Sharing","Non AC 2-Sharing"),
        ("Non AC 3-Sharing","Non AC 3-Sharing"),
    ]
    ps=[
        ("Not Paid","Not Paid"),
        ("Paid","Paid"),
    ]
    st=[
        ("Monthly","Monthly"),
        ("Guest","Guest"),
    ]
    rn=[
        ("select","select"),
    ]
    Name=m.CharField(max_length=50)
    profession=m.CharField(max_length=30,choices=p)
    year=m.IntegerField(null=True)
    mobile=m.CharField(max_length=10)
    email=m.CharField(max_length=50)
    aadhar=m.CharField(max_length=12)
    room_no=m.CharField(max_length=10,choices=rn)
    DOJ=m.DateField(auto_now_add=True)
    room_type=m.CharField(max_length=30,choices=rt)
    fee=m.IntegerField()
    payment_status=m.CharField(max_length=20,choices=ps)
    stay_type=m.CharField(max_length=20,choices=st,default="Monthly")

class Problem(m.Model):
    s=[
        ("Viewed","Viewed"),
        ("Not Viewed","Not Viewed")
    ]
    username=m.CharField(max_length=40)
    email=m.CharField(max_length=40,null=True)
    room_no=m.CharField(max_length=10)
    issue=m.CharField(max_length=200)
    status=m.CharField(max_length=10,choices=s,default="Not Viewed")
