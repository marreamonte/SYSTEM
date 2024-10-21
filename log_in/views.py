from django.shortcuts import render

# Create your views here.

def login(responsed):
    return render(responsed, 'login/login.html')