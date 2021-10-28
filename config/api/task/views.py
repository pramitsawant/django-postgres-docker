from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("task Home!")
def get(request,pk):
    return HttpResponse("task id!"+pk)   