from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth.models import *
from django.contrib import auth,messages
from . models import *

def demo(request):
    return render(request,'demo.html')

