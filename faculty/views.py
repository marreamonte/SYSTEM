from django.shortcuts import render
# Create your views here.

def faculty_dashboard(request):
    return render(request, 'faculty_dashboard/faculty_dashboard.html')

def master_list(request):
    return render(request, 'faculty_dashboard/master_list.html')

def acads_record(request):
    return render(request, 'faculty_dashboard/acads_record.html')

def account_setting(request):
    return render(request, 'faculty_dashboard/account_setting.html')

def settings(request):
    return render(request, 'faculty_dashboard/setting.html')