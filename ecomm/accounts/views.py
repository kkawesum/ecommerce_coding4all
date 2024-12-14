from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import  HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import Profile

def login_page(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)
        
        if not user_obj.exists():
            messages.warning(request,'Profile not found')
            return HttpResponseRedirect(redirect_to=request.path_info)
        
        if not user_obj[0].is_email_verified:
            messages.warning(request,'Your account is not verified')
            return HttpResponseRedirect(redirect_to=request.path_info)
        
        user_obj = authenticate(username=email,password = password)
        if user_obj:
            login(request=request,user=user_obj)
            return redirect('/')
        
        messages.warning(request,'Invalid credentials')
        return HttpResponseRedirect(redirect_to=request.path_info)
    return render(request,'accounts/login.html')


def register_page(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=email)
        if user_obj.exists():
            messages.warning(request,'Email is already registered')
            return HttpResponseRedirect(redirect_to=request.path_info)
        
        messages.success(request,'An email has been sent. Please activate the account')
    return render(request,'accounts/register.html')