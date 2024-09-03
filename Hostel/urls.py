from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns=[
    path("tenants",v.tenantsList,name="T_List"),
    path('registration/',v.register,name="register"),
    path('update/<int:p>',v.update,name="update"),
    path('del/<int:t>',v.delete,name="delete"),
    path('problems_list',v.problems_list,name="problems_list"),
    path("problem",v.problem,name="problem"),
    path("probleminfo/<int:id>",v.probleminfo,name="probleminfo"),
    path("menu",v.menu,name="menu"),
    path("rules",v.rules,name="rules"),
    path("add_hostel_room",v.add_hostel_room,name="addroom"),
    path("delconf/<int:tid>",v.delconf,name="delconf"),
    path("send_reply/<str:email>",v.send_reply,name="send_reply"),
    path("delprob/<int:id>",v.delprob,name="delprob"),

]