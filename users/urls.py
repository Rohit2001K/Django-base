from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('sub/<str:pk>',views.sub,name='subsite'),
    path('login/',views.loginpage,name='loginpage'),
    path('logout/',views.logoutpage,name='logoutpage'),
    path('users/',views.checking,name='check'),
    path('signup/',views.signup,name='signup'),
    path('edit/',views.account,name='edit'),
    path('ed/',views.home)
]