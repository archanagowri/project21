from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sunny(request,name,age):
    return HttpResponse(f'Welcome to the page {name}/n {age}')