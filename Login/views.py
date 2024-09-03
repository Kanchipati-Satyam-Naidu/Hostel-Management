from django.shortcuts import render,redirect
from Login.forms import *
from Login import models as lm
from Hostel import models as hm
from django.contrib import auth
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from Hostel import forms as hf

# Create your views here.
email_from = settings.EMAIL_HOST_USER

def home(request):
    p=hm.Problem.objects.filter(status="Not Viewed")
    return render(request,"home.html",{"problems":p})

def signUp(request):
    f=User_SignUp()
    ms=" "
    if request.method=="POST":
        if lm.User.objects.filter(username=request.POST["username"]).exists():
            f=User_SignUp(request.POST)
            ms="Username Already Exists...!"

        elif not(hm.Tenants.objects.filter(email=request.POST["email"]).exists()):
            ms="You can't sign up as you are not a member of our hostel or if you are member give the correct email"
        else:
            # form=request.POST.copy()
            # rn=hm.Tenants.objects.get(email=request.POST["email"])
            # form["room_no"]=rn.room_no
            f=User_SignUp(request.POST)
            if f.is_valid():
                # sub='Succesfully Account Created....!'
                # message = f'Hi {request.POST["username"]} thank you for Signing up to our Hostel Website.\n-:Details:-\nFirst Name: {request.POST["first_name"]}\nLast Name: {request.POST["last_name"]}\n'
                # recipient_list = [request.POST["email"], ]
                # email_from = settings.EMAIL_HOST_USER
                # send_mail( sub, message, email_from, recipient_list )
                f.save()
                return redirect('login')
            else:
                ms="Invalid Password Credentials..!"
    return render(request,"signup.html",{"fields":f,"ms":ms})  

def User_Login(request):
    if request.method=="POST":
        name=request.POST["username"]
        e_password=request.POST["password"]
        user=auth.authenticate(request,username=name,password=e_password)
        if user is not None:
            auth.login(request,user)
            # sub='Succesfully Logged in....!'
            # message = f'Hi {user.username}, thank you for Logging into Hostel Website.'
            # recipient_list = [user.email,]
            # send_mail( sub, message, email_from, recipient_list )
            return redirect('home')
        return render(request,"user_login.html",{"msg":"Invalid Username or Password"})
    return render(request,"user_login.html",{"msg":" "})

def logout(request):
    # if request.method=="POST":
    #     auth.logout(request)
    #     return redirect('home')
    return render(request,"logout.html")

def lgoconf(request):
    auth.logout(request)
    return redirect('home')


def contact(request):
    return render(request,"contact_us.html")

def rooms(request):
    d={}
    fr=hm.Hostel.objects.order_by('-floor_no').first()
    f=[]
    for i in range(1,fr.floor_no+1):
        f.append(i)
    if request.method=="POST":
        tor=request.POST.get("search")
        if tor=="all":
            pass
        else:
            for i in f:
                d[i]=list(hm.Hostel.objects.filter(room_type=tor,floor_no=i))
            return render(request,"rooms.html",{"floors":f,"flats":d,"ty":tor})

    for i in f:
        d[i]=list(hm.Hostel.objects.filter(floor_no=i))
    return render(request,"rooms.html",{"floors":f,"flats":d})
    
@login_required
def hostel_room_info(request,rno):
    if request.method=="POST":
        room=hm.Hostel.objects.get(room_no=rno)
        ri=hf.HostelRoom(request.POST,instance=room)
        if ri.is_valid():
            ri.save()
            return redirect('rooms')
    room=hm.Hostel.objects.get(room_no=rno)
    ri=hf.HostelRoom(instance=room)
    return render(request,"info.html",{"f":ri,"rn":rno})

@login_required
def delete_hostel_room(request,rno):
    room=hm.Hostel.objects.get(room_no=rno)
    # if request.method=="POST":
    #     room.delete()
    #     return redirect('rooms')
    return render(request,"delete.html",{"t":"room","rno":room.room_no})

def drmconf(request,rno):
    room=hm.Hostel.objects.get(room_no=rno)
    t=Tenants.objects.filter(room_no=rno)
    u=User.objects.filter(room_no=rno)
    for i in t:
        i.delete()
    
    for i in u:
        i.delete()

    room.delete()
    return redirect('rooms')


@login_required
def info(request,id):
    u=lm.User.objects.get(id=id)
    form=User_info(instance=u)
    rd=hm.Hostel.objects.get(room_no=u.room_no)
    if request.method=="POST":
        form=User_info(request.POST,instance=u)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,"info.html",{"f":form,"rd":rd})

@login_required
def feedback(request):
    f=lm.Feedback.objects.all()
    r=0
    if len(f)!=0:
        for i in f:
            r+=i.rating
        r=round(r/len(f),1)
    return render(request,"feedback.html",{"fb":f,"rating":r})

@login_required
def feedbackform(request):
    f=FeedbackForm()
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
        else:
            print(request.POST["description"])
            print(request.POST.get("email"))
            print("Invalid form")
    return render(request,"feedbackform.html",{"form":f})

def about_us(request):
    return render(request,"about_us.html")