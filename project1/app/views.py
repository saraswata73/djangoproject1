from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HOME(request):
    return HttpResponse('this is home page')
def LOGIN(xyz):
    return HttpResponse('this is login page')
def LOGOUT(abc):
    return HttpResponse('this is logout')