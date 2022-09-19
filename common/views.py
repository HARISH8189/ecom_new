import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'commontemplates/index.html')

def seller_login(request):
    return render(request, 'commontemplates/seller_login.html')

def customer_login(request):
    return render(request, 'commontemplates/customer_login.html')

def seller_signup(request):
    return render(request, 'commontemplates/seller_signup.html')

def customer_signup(request):
    return render(request, 'commontemplates/customer_signup.html')          

def change_password(request):
    return render(request, 'commontemplates/change_password.html')

def name(request):
    return render(request, 'commontemplates/name.html')    