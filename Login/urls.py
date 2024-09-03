from django.urls import path
from Login import views as lv

urlpatterns=[
    path("signup",lv.signUp,name="sign"),
    path("userlog",lv.User_Login,name="login"),
    path('',lv.home,name="home"),
    path('logout',lv.logout,name="logout"),
    path('contact',lv.contact,name="contact"),
    path('rooms',lv.rooms,name="rooms"),
    path('info/<int:id>',lv.info,name="info"),
    path('room_info/<str:rno>',lv.hostel_room_info,name="room_info"),
    path("about-us",lv.about_us,name="about-us"),
    path("delete_room/<str:rno>",lv.delete_hostel_room,name="delete_room"),
    path("feedback",lv.feedback,name="feedback"),
    path("feedbackform",lv.feedbackform,name="feedbackform"),
    path("drmconf/<str:rno>",lv.drmconf,name="drmconf"),
    path("lgoconf",lv.lgoconf,name="lgoconf"),
]
