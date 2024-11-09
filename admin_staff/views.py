from django.shortcuts import render, redirect
from .models import StudentProfile, FacultyStaff, Announcement, AdminStaff, AdmissionStaff,  GuidanceStaff, RegistrarStaff, section
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
    

#announcement
@login_required(login_url='login')
@admin_only
def admin_dashboard(request):
    announcement = Announcement.objects.all()
    return render(request, 'admin/admin_dashboard.html', { 'announcement': announcement })

def edit_annoucement(request, id):
    announcement = Announcement.objects.get(announcement_id = id)
    return render(request, 'admin/editannouncement.html', { 'announcement': announcement })

def update(request, id):
    newtitle = request.POST['title']
    newbody = request.POST['body']

    users = Announcement.objects.get(announcement_id = id)

    users.body = newbody
    users.title = newtitle
    users.save()
    return redirect('/')



@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def classes(request):
    return render(request, 'admin/classes.html')



#student
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



#student end
@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def student_dashboard(request):
    announcement = Announcement.objects.all()
    context = {'announcement':announcement}
    return render(request, 'student/student_dashboard.html', context)


@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def student_profile(request):
    student = request.user.studentprofile
    context = {'student': student}
    return render(request, 'student/student_profile.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def setting(request):
    student = request.user.studentprofile
    context = {'student': student}
    return render(request, 'student/settings.html', context)
