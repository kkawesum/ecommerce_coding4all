from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import  HttpResponseRedirect
# Create your views here.

def login_page(request):
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