from django.shortcuts import render,redirect
from .models import profiles
from .models import skills
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import customsignup
# Create your views here.

def home(request):
    user_info=profiles.objects.all()
    return render(request,'pages/home.html',{'user_info':user_info})


def sub(request,pk):
    user_info=profiles.objects.filter(id=pk)

    return render(request,'pages/sub.html',{'user_info':user_info})


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'USername or password is wrong')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'USername or password is wrong')
    return render(request,'pages/login.html')

@login_required(login_url='loginpage')
def checking(request):
    return HttpResponse("This is for login users only")

def logoutpage(request):
    messages.success(request, "Logout succ")
    logout(request)
    return redirect('loginpage')


def signup(request):
    form=customsignup()
    if request.method=='POST':
        form=customsignup(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'User account was created')
            login(request,user)
            return redirect('home')
    return render(request,'pages/signup.html',{'form':form})


def account(request):
    userss=request.user.accounts

    return render(request,'pages/account.html',{'userss':userss})