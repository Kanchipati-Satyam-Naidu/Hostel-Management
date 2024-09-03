from django import forms
from .models import *

class Registration(forms.ModelForm):
    class Meta:
        model=Tenants
        fields=["Name","profession","year","mobile","email","aadhar","stay_type","room_type","room_no","fee","payment_status"]
        widgets={
            
            "Name":forms.TextInput(attrs={
                "class":"form-control mt-0 mb-3 my-1",
                "placeholder":"Enter Name",
                "style":"width:250px;"
            }),

            "profession":forms.Select(attrs={
                "class":"form-control mt-0 mb-3 my-1",
                "style":"width:250px;font-weight: bold;text-align:center;"
            }),
            "year":forms.TextInput(attrs={
                "class":"form-control mt-0 mb-3 my-1",
                "placeholder":"Enter Year",
                "style":"width:250px;"
            }),
            "mobile":forms.TextInput(attrs={
                "class":"form-control mt-0 my-1",
                "placeholder":"Enter Mobile Number",
                "style":"width:250px;"
            }),

            "email":forms.EmailInput(attrs={
                "class":"form-control mt-0 my-1",
                "placeholder":"Enter mail id",
                "style":"width:250px;"
            }),

            "aadhar":forms.TextInput(attrs={
            "class":"form-control mt-0 my-1",
            "placeholder":"Enter Aadhar Number",
            "style":"width:250px;"
            }),

            "room_type":forms.Select(attrs={
                "class":"form-control mt-0 my-1",
                "style":"width:250px;font-weight: bold;text-align:center;"
            }),

             "room_no":forms.Select(attrs={
                "class":"form-control mt-0 my-1",
                "style":"width:250px;"
            }),             
            
            "fee":forms.NumberInput(attrs={
                "class":"form-control mt-0 my-1",
                "placeholder":"Enter Fee",
                "style":"width:250px;"
            }),

            "payment_status":forms.Select(attrs={
                "class":"form-control mt-0 my-1",
                "style":"width:250px;font-weight: bold;text-align:center;"
            }),

            "stay_type":forms.Select(attrs={
                "class":"form-control mt-0 my-1",
                "onchange":"feecal()",
                "style":"width:250px; font-weight: bold;text-align:center;"
            }),
            
        }

class HostelRoom(forms.ModelForm):
    class Meta:
        model=Hostel
        fields=["floor_no","room_no","room_type","room_status","total_no_of_beds","no_of_beds_ava","fee"]
        widgets={
            "floor_no":forms.NumberInput(attrs={
                "class":"form-control mt-3 my-1",
                "placeholder":"Enter Flat No",
            }),
            "room_no":forms.TextInput(attrs={
                "class":"form-control mt-3 my-1",
                "placeholder":"Enter Room No",
                
            }),
            "room_type":forms.Select(attrs={
                "class":"form-control mt-3 my-1",
               
            }),
            "room_status":forms.Select(attrs={
                "class":"form-control mt-3 my-1",
                
            }),
            "total_no_of_beds":forms.NumberInput(attrs={
                "class":"form-control mt-3 my-1",
                "placeholder":"Enter Total no of beds",
                
            }),
            "no_of_beds_ava":forms.NumberInput(attrs={
                "class":"form-control mt-3 my-1",
                "placeholder":"Enter no of beds Available", 
            }),

            "fee":forms.NumberInput(attrs={
                "class":"form-control mt-3 my-1",
                "placeholder":"Enter Fee", 
            }),

        }

class ProblemForm(forms.ModelForm):
    class Meta:
        model=Problem
        fields=["username","room_no","issue","email"]
        

