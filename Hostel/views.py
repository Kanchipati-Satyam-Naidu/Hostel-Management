from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from . models import *
from Login.models import *
from Hostel.forms import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
import json
# Create your views here.

email_from = settings.EMAIL_HOST_USER

@login_required
def tenantsList(request):
    if request.method=="POST":
        tot=request.POST.get('search')
        if tot=="all":
            t=Tenants.objects.all()
        elif tot=="Not Paid":
            t=Tenants.objects.filter(payment_status="Not Paid")
        elif tot=="Paid":
            t=Tenants.objects.filter(payment_status="Paid")
        elif tot=="Guest":
            t=Tenants.objects.filter(stay_type="Guest")
        else:
            t=Tenants.objects.filter(stay_type="Monthly")
        return render(request,"Tenants_List.html",{"tenants":t})
    t=Tenants.objects.all()
    return render(request,"Tenants_List.html",{"tenants":t})


@login_required
def register(request):
    if request.method=="POST":
        r=Registration(request.POST)
        if r.is_valid():
            rno=request.POST["room_no"]
            # rty=request.POST["room_type"]
            # rf=request.POST["fee"]
            # sub='Joined Successfully....!'
            # message = f'Hi {request.POST["Name"]}, thank you for choosing our Hostel\nYour room no is {rno}, {rty}\nFee :{rf} \nPayment Status:{request.POST["payment_status"]}.'
            # recipient_list = [request.POST["email"], ]
            # send_mail( sub, message, email_from, recipient_list )
            room=Hostel.objects.get(room_no=rno)
            room.no_of_beds_ava-=1
            if room.no_of_beds_ava==0:
                room.room_status="Full/Unavailable"
            r.save()
            room.save()
            return redirect("T_List")

    r=Registration()
    l=["AC 2-Sharing","AC 3-Sharing","Non AC 2-Sharing","Non AC 3-Sharing"]
    rooms={}
    for i in l:
        rooms[i]=list(Hostel.objects.filter(room_type=i,room_status="Available").values_list('room_no', flat=True))
    r1=json.dumps(rooms)
    return render(request,"Tenants_Register.html",{"fields":r,"rooms":r1})

        

@login_required
def update(request,p):
    t=Tenants.objects.get(id=p)
    person=Registration(instance=t)
    if request.method=="POST":
        person=Registration(request.POST,instance=t)
        if person.is_valid():
            person.save()
            return redirect("T_List")
    return render(request,"update.html",{"tenants":person,"t":t})

@login_required
def delete(request,t):
    person=Tenants.objects.get(id=t)
    # if request.method=="POST":
    #     room=Hostel.objects.get(room_no=person.room_no)
    #     room.no_of_beds_ava+=1
    #     room.room_status="Available"
    #     room.save()
    #     person.delete()
    #     return redirect('T_List')
    return render(request,"delete.html",{"t":"hosteler","name":person.Name,"tid":t})

@login_required
def delconf(request,tid):
    person=Tenants.objects.get(id=tid)
    user=User.objects.filter(email=person.email)
    room=Hostel.objects.get(room_no=person.room_no)
    room.no_of_beds_ava+=1
    room.room_status="Available"
    if user.exists():
        user.delete()
    room.save()
    person.delete()
    return redirect('T_List')



def menu(request):
    return render(request,"menu.html")

def rules(request):
    return render(request,"rules.html")

@login_required
def add_hostel_room(request):
    if request.method=="POST":
        room=HostelRoom(request.POST)
        if room.is_valid():
            room.save()
            return redirect("rooms")
    room=HostelRoom()
    return render(request,"Add_rooms.html",{"room":room})


def problem(request):
    if request.method=="POST":
        f=ProblemForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('home')
    return render(request,"problem.html")

def problems_list(request):
    p=Problem.objects.all()
    return render(request,"problems_list.html",{"problems":p})

@login_required
def probleminfo(request,id):
    p=Problem.objects.get(id=id)
    if request.method=="POST":
        p.status="Viewed"
        p.save()
        return redirect('home')
    return render(request,"probleminfo.html",{"f":p})

def send_reply(request,email):
    if request.method=="POST":
        message=request.POST["message"]
        sub="Problem will be solved"
        print(email)
        rl=[email,]
        send_mail( sub, message, email_from, rl )
        return redirect('home')

    return render(request,"send_reply.html",{"email":email})

def delprob(request,id):
    p=Problem.objects.get(id=id)
    p.delete()
    return redirect('problems_list')


def avail_Rooms(request,type):
    h=Hostel.objects.filter(room_type=type,status="Available").values_list('room_no',flat=True)
    