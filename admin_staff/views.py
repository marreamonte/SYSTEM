from django.shortcuts import render, redirect
from .models import StudentProfile, FacultyStaff, Announcement
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user, admin_only

# Create your views here.


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST['username'];
        password = request.POST['password'];
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("invalid username or password, try again"))
            return redirect('login')      
    else:
        context = {}    
        return render(request, 'login/login.html', context )
    

def logout_user(request):
    logout(request)
    return redirect('login')
    

#announcement_admin
@login_required(login_url='login')
@admin_only
def admin_dashboard(request):
    announcement = Announcement.objects.all()
    return render(request, 'admin/admin_dashboard.html', { 'announcement': announcement })

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def classes(request):
    
    return render(request, 'admin/classes.html', )

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def student_list(request):
    students = StudentProfile.objects.all()
    return render(request, 'admin/student_list.html', { 'student': students})

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def student(request, pk):
    student = StudentProfile.objects.get(student_lrn = pk)
    return render(request, 'admin/student_profile.html', {'student': student})


@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def faculty_list(request):
    faculty = FacultyStaff.objects.all()
    return render(request, 'admin/faculty_list.html', { 'faculty': faculty})

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def faculty_profile(request, pk):
    faculty = FacultyStaff.objects.get(faculty_staff_id = pk)
    return render(request, 'admin/faculty_profile.html', {'faculty': faculty})

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def accademic_record(request):
    return render(request, 'admin/academic_record.html')

def anecdotal_record(request):
    return render(request, "admin/anecdotal_record.html")


#accounting end
def financial_record(request):
    return render(request, "accounting/financial_record.html")


#student end
@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def student_dashboard(request):
    
    student = request.user.studentprofile
    context = { 'student': student}
    return render(request, 'student/student_dashboard.html', context)


@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def student_profile(request):
    student = request.user.studentprofile
    return render(request, 'student/student_profile.html', {'student': student})




#faculty end
@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def faculty_dashboard(request):
    adviser = request.user.facultystaff
    context = {'adviser': adviser}
    return render(request, 'faculty/faculty-dashboard.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def advisory(request):
    advisoryClass = request.user.facultystaff.studentprofile_set.all()
    adviser = request.user.facultystaff
    context = {'advisoryClass': advisoryClass, 'adviser':adviser}
    return render(request, 'faculty/student_list.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def student_records(request):
    return render(request, 'faculty/record.html')

@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def student_info(request):
    return render(request, 'faculty/record.html')

@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def faculty_info(request):
    adviser = request.user.facultystaff
    context = {'adviser': adviser}
    return render(request, 'faculty/faculty_profile.html', context)

