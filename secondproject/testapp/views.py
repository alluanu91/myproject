from django.shortcuts import render
from django.http import HttpResponse
import datetime
# def Create your views here.
def hello(request):
    t=datetime.datetime.now()
    s='<h1> data and time now is :'+ str(t)+'</h1>'
    return HttpResponse(s)
def good_morning(request):
    return HttpResponse("hello good morning")
def good_afternoon(request):
    return HttpResponse("hello good afternoon")
def good_night(request):
    return HttpResponse("hello good night ")
