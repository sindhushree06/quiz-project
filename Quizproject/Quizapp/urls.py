from django.urls import path
from . import views

urlpatterns=[

     path('',views.index,name="index"),
     path('login',views.login,name="login"),
     path('register',views.register,name="register"),
     path('logout',views.logout,name="logout"),
     path('about',views.about,name="about"),
     path('front',views.front,name='front'),
     path('ds',views.ds,name='ds'),
     path('os',views.os,name='os'),
     path('oop',views.oop,name='oop'),
     path('cns',views.cns,name='cns'),
     path('dbms',views.dbms,name='dbms'),
     path('co',views.co,name='co'),
     path('profile',views.profile,name='profile'),
     path('profile-edit',views.editProfile,name='profile-edit'),
     path('delete',views.deleteProfile,name='deleteProfile')

]