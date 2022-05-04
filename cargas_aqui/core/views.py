from django.shortcuts import render
from django.http import HttpResponse

def showLogin(request):
    return render(request, 'auth/login.html')

def listCargas(request):
    return render(request, 'cargas/list.html')