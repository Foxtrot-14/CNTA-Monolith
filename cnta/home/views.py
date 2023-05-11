from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from . utils import send_otp
from . models import Profile,Child
import http.client
from django.contrib.auth.decorators import login_required
import random

def index(request):
    return render(request, 'index.html')
def loginpage(request):
    return render(request, 'login.html')
@login_required(login_url='home-login')
def report(request,pk):
    return render(request,'report.html')
def registerform(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        mobile = request.POST.get('user_number')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password2')
        check_user = Profile.objects.filter(mobile=mobile).first()
        check_name = User.objects.filter(username=name).first()
        if check_name:
            context = { 'userexists':'User alredy exists with this name, choose a unique name' }
            return render(request, 'login.html',context)
        if check_user:
            context = { 'phoneexists':'User alredy exists with this phone number' }
            return render(request, 'login.html',context)
        if pass1 != pass2:
            context = { 'passm':'The passwords did not match' }
            return render(request, 'login.html',context)
        
        otp = random.randint(1000,9999)
        ##send_otp(mobile=mobile,otp=otp)
        pass1 = make_password(pass1)
        user = User(first_name=name,username=name,password=pass1)
        user.save()
        profile = Profile(user=user,mobile=mobile,otp=otp)
        profile.save()
        request.session['mobile']=mobile
        request.session['name']=name
        return redirect('home-otp')
    return HttpResponse('404 - Not Found') 
def otp(request):
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    if request.method == 'POST':
        b_otp = request.POST.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()
        if b_otp == profile.otp:
            context = {'created':'User created successfully. Log In to continue'}
            return render(request,'login.html',context)
        else:
            context = {'message':'You have entered wrong OTP'}
            return render(request,'otp.html',context)
        
    return render(request, 'otp.html',context)
def loginform(request):
    if request.method == 'POST':
        log_mobile = request.POST.get('log_number')
        log_passw =  request.POST.get('log_passw')
        profile = Profile.objects.filter(mobile=log_mobile).first()
        user = authenticate(username = profile.user.username,password=log_passw)
        if user is not None:
            login(request, user)
            return redirect('home-user')
        else:
            return redirect('home-login')
    return HttpResponse('404 - Not Found')  
@login_required(login_url='home-login')
def logoutbutton(request):
    logout(request)
    return redirect('home-index') 
@login_required(login_url='home-login')
def child(request):   
    if request.method == 'POST':
        image = request.FILES.get('image')
        Fname = request.POST.get('FName')
        Lname = request.POST.get('LName')
        Sex = request.POST.get('Sex')
        Father = request.POST.get('Father')
        fnumber = request.POST.get('fnumber')
        mother = request.POST.get('mother')
        mnumber = request.POST.get('mnumber')
        age = request.POST.get('age')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        headcir = request.POST.get('headcir')
        muac = request.POST.get('muac')
        chestCir = request.POST.get('chestCir')
        date = request.POST.get('date')
        child = Child(fName=Fname,lName=Lname,sex=Sex,father=Father,fnumber=fnumber,mother=mother,
                    mnumber=mnumber,age=age,weight=weight,height=height,headcir=headcir,
                    muac=muac,chestCir=chestCir,date=date,adder=request.user.username,image=image)
        child.save()
    return render(request,'child.html')       
@login_required(login_url='home-login')
def user(request):
    name = request.user.username
    child = Child.objects.all().filter(adder=name)
    context = {
        'name':name,
        'childs': child,
    }
    return render(request,'user.html', context)