from django.shortcuts import render

# Create your views here.

def dashboard(respond):
    return render(respond, 'dashboard/dashboard.html')

def profile(respond):
    return render(respond, 'dashboard/profile.html')

def academic(respond):
    return render(respond, 'dashboard/academic.html')

def bill(respond):
    return render(respond, 'dashboard/bill.html')
