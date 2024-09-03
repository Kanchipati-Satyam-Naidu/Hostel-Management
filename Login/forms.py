from . models import User,Feedback
from django import forms
from django.db import models as m
from django.contrib.auth.forms import UserCreationForm

class User_SignUp(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
               "class":"form-control mt-1 my-1",
                "placeholder":"Enter Password",
             }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
               "class":"form-control mt-1 my-1",
                "placeholder":"Confirm Password",
             }))
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","mobile","room_no"]
        widgets={
             "first_name":forms.TextInput(attrs={
                "class":"form-control mt-2 my-1",
                'placeholder':"Enter First Name:",

             }),
             "last_name":forms.TextInput(attrs={
                "class":"form-control mt-2 my-1",
                'placeholder':"Enter Last Name:",

             }),
             "username":forms.TextInput(attrs={
                "class":"form-control mt-2 my-1",
                'placeholder':"Enter User Name:",
             }),
             
             "email":forms.TextInput(attrs={
                'class':"form-control mt-2 my-3",
                'placeholder':"Enter email",
             }),

             "mobile":forms.TextInput(attrs={
             "class":"form-control mt-2 my-1",
             "placeholder":"Enter Mobile Number",
             }),
             
             "room_no":forms.TextInput(attrs={
               "class":"form-control mt-2 my-1",
               "placeholder":"Enter Room Number",
             })
         }


class User_info(forms.ModelForm):
   class Meta:
        model=User
        fields=["first_name","last_name","username","email","mobile","room_no"]
        widgets={
             "first_name":forms.TextInput(attrs={
                "class":"form-control mt-0 mb-3 my-1",
                'placeholder':"NULL",
                

             }),
             "last_name":forms.TextInput(attrs={
                "class":"form-control mt-0 mb-3 my-1",
                'placeholder':"NULL",
                

             }),
             "username":forms.TextInput(attrs={
                "class":"form-control mt-0 mb-3 my-1",
                'placeholder':"NULL",
                
             }),
             
             "email":forms.EmailInput(attrs={
                'class':"form-control mt-0 mb-3 my-3",
                'placeholder':"NULL",
                
             }),

             "mobile":forms.TextInput(attrs={
             "class":"form-control mt-0 mb-3 my-1",
             "placeholder":"NULL",
             
             }),

             "room_no":forms.TextInput(attrs={
               "class":"form-control mt-0 mb-3 my-1",
             })
             
         }
class FeedbackForm(forms.ModelForm):
   class Meta:
        model=Feedback
        fields=["email","description","rating"]
        
