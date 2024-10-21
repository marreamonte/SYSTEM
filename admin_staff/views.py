from django.shortcuts import render, redirect
from .models import StudentProfile, Annoucement, AdminStaff, AdmissionStaff, FacultyStaff, GuidanceStaff, RegistrarStaff

# Create your views here.

#announcement
def admin_dashboard(request):
    annoucement = Annoucement.objects.all()
    return render(request, 'admin/admin_dashboard.html', { 'annoucement': annoucement})

def annoucement(request, id):
    annoucement = Annoucement.objects.get(annoucement_id = id)
    return render(request, 'admin/editannouncement.html', {'annoucement': annoucement})

def update_announcement(request, id):
    newtile = request.POST['title']
    newbody = request.POST['body']
    accouncement = Annoucement.objects.get(annoucement_id = id)
    accouncement.title = newtile
    accouncement.body = newbody
    accouncement.save()
    return redirect('/')






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




