#Creating Endpoints
#In words of API Endpoints means urls

from django.urls import path
from . import views



urlpatterns = [
    path('get',views.getData,name = 'getdata'),
    path('get/python',views.getPython,name = 'getdata'),
    path('get/java',views.getJava,name = 'getdata'),
    path('get/testing',views.getTesting,name = 'getdata'),
    path('get/dev',views.getDev,name = 'getdata'),
    path('post/',views.insertData,name = 'insertdata'),
    path('join/',views.getjoin,name = 'insertjoindata'),
    path('joinpost/',views.insertjoinData,name = 'insertjoindata'),
    path('joinget/<int:pk>',views.getjoinData,name = 'getjoindata'),
    path('contact/',views.contactData,name = 'contactdata'),
    path('demopost/',views.demoData,name = 'demodata'),
    path('getdemo/',views.getdemoData,name = 'getdemodata'),
    path("userlogin/",views.userLogin),
    path("getuser/",views.getUser),
    path("adminlogin/",views.adminLogin),
    path("superlogin/",views.superLogin),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    

    
]