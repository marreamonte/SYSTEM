from django.shortcuts import render, redirect
from .models import StudentProfile, Announcement, AdminStaff, AdmissionStaff, FacultyStaff, GuidanceStaff, RegistrarStaff
from django.shortcuts import render, get_object_or_404
# Create your views here.

#announcement
def admin_dashboard(request):
    announcement = Announcement.objects.all()
    return render(request, 'admin/admin_dashboard.html', { 'announcement': announcement })

def edit_annoucement(request, id):
    announcement = get_object_or_404(Announcement, announcement_id = id)
    return render(request, 'admin/editannouncement.html', { 'announcement': announcement })

def update(request, id):
    newtitle = request.POST['title']
    newbody = request.POST['body']

    users = Announcement.objects.get(announcement_id = id)

    users.body = newbody
    users.title = newtitle
    users.save()
    return redirect('/')





















def classes(request):
    return render(request, 'admin/classes.html');



#student
def student_list(request):
    students = StudentProfile.objects.all()
    return render(request, 'admin/student_list.html', { 'student': students})

def student_profile(request, pk):
    student = StudentProfile.objects.get(student_lrn = pk)
    return render(request, 'admin/student_profile.html', {'student': student})







def faculty_list(request):
    faculty = FacultyStaff.objects.all()
    return render(request, 'admin/faculty_list.html', { 'faculty': faculty})




