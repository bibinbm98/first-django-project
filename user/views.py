from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"user/home.html")

def registration(request):
    return render(request,"user/registration.html")

def login(request):
    return render(request,"user/login.html")