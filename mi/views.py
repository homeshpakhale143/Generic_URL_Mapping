from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mi(request):
    return render(request,'sachin.html')

def mi_team(request):
    return HttpResponse('My Favourite Team')
