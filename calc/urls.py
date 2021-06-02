"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path
from .views import addition_page,subtraction_page,multiplication_page,division_page,index

urlpatterns = [
    path("add",addition_page,name="getaddition"),
    path("sub",subtraction_page,name="getsubtraction"),
    path("mul",multiplication_page,name="getmultiplication"),
    path("div",division_page,name="getdivision"),
    path("index", index, name="index"),

]
