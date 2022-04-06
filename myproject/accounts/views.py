from django.shortcuts import render,redirect
from .forms import *
from .models import MyUser
from django.contrib import messages
# Create your views here.

def register_admin(req):
    if req.method=='POST':
        form = AdminForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"Admin Register Successfully...")
            return redirect("Login")
        else:
            messages.error(req,"Registration Unsuccessfull, Something went wrong...")
    else:
        form = AdminForm()
    context = {'form':form}
    return render(req,'accounts/registration.html',context)

    
def register_customer(req):
    if req.method=='POST':
        form = UserForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"Your registrations is Successfull.")
            return redirect("Login")
        else:
            messages.error(req,"Registration Unsuccessfull, Something went wrong...")
    else:
        form = UserForm()
    context = {'form':form}
    return render(req,'accounts/registration.html',context)

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
def mylogin(req):
    print(req.method)
    if req.method=='POST':
        form = AuthenticationForm(req.POST)
        mobile_Number = req.POST['username']
        password = req.POST['password']
        if mobile_Number and password and mobile_Number.isdigit():
            user = authenticate(req,username=mobile_Number,password=password)
            if user:
                login(req,user)
                messages.success(req,"Login Successfull.")
                return redirect("Home")
            else:
                messages.error(req,"Invalid Mobile Number or Password")
        else:
            messages.error(req,"please Enter the Mobile and Password")
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(req,'accounts/login.html',context)


def mylogout(req):
    logout(req)
    messages.warning(req,"Logout Successfull...")
    return redirect("Home")


def profile(req,userId):
    if req.method=='GET':
        acc=MyUser.objects.get(userId=userId)
        form= UserForm(instance=acc)
        context={'form':form}
        return render(req,"accounts/profile.html",context)
    elif req.method=='POST':
        acc=MyUser.objects.get(userId=userId)
        form=UserForm(data=req.POST,instance=acc)
        if form.is_valid():
            form.save()
            messages.success(req,'your profile is updated.')
            return redirect('Home')
    else:
        context={'form':form}
        messages.error(req,"somethong went wrong try again")
        return render(req,'accounts/profile.html',context)



def review(req):
    return render(req,"accounts/review.html")

import random
def rand():
    n=random.randint(1000,9999)
    return n

#send otp as a text msg via twilio
from twilio.rest import Client
def otp(mob):
    mob=mob
    account_sid='your twilio sid here'
    auth_token='your twilio auth token here'
    client=Client(account_sid,auth_token)
    m1="otp for resetting password is:"
    global OTP
    m2=str(rand())
    OTP=m2
    m=m1+m2
    d2='+91'
    d1=d2+mob
    message=client.messages.create(body=m,from_="+16067160394",to=d1)
    return OTP


def sendotp(req):
    if req.method=='POST':
        mobile=req.POST['mobile']
        onetimepassword=otp(mobile)
        req.session.setdefault("onetimepassword",onetimepassword)
        req.session.setdefault("usermobile",mobile)
        return redirect('otp')

def getotp(req):
    if req.method=='GET':
        return redirect('otpget')
    if req.method=='POST':
        userotp=int(req.POST['otp'])
        sysotp=int(req.session['onetimepassword'])
        mob=req.session['usermobile']
        if userotp==sysotp:
            acc=MyUser.objects.get(mobile_Number=mob)
            form= UserForm(instance=acc)
            context={'form':form}
            messages.success(req,"update your account")
            del req.session['sysotp']
            return render(req,'accounts/profile.html',context)
        else:
            messages.error(req,"otp is not valid")
            return redirect('Home')

def setpassword(req):
    if req.method=='POST':
        mob=req.session['mobile']
        acc=MyUser.objects.get(mobile_Number=mob)
        form=UserForm(data=req.POST,instance=acc)
        if form.is_valid():
            form.save()
            messages.success(req,'your profile is updated.')
            return redirect('Home')
    else:
        messages.error(req,"something went wrong try after some time")
        return redirect('Home')