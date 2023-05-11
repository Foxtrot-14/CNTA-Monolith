from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name='home-index'),
    path("login", views.loginpage,name='home-login'),
    path("registerform",views.registerform,name='registerform'),
    path("loginform",views.loginform,name='loginform'),
    path("report",views.report,name='home-report'),
    path("otp",views.otp,name='home-otp'),
    path("user",views.user,name='home-user'),
    path("logoutbutton",views.logoutbutton,name='home-logoutbutton'),
    path("child/",views.child,name='home-child'),
]
