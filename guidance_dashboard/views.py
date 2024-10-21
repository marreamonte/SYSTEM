from django.shortcuts import render

# Create your views here.

def guidanceDashboard(request):
    return render(request, 'dashboard/guidance_dashboard.html')

def studentList(request):
    return render(request, 'dashboard/grade_Seven.html')

def gradeeight(request):
    return render(request, 'dashboard/grade_eight.html')

def gradenine(request):
    return render(request, 'dashboard/grade_nine.html')

def gradeten(request):
    return render(request, 'dashboard/grade_ten.html')

def studentProfile(request):
    return render(request, 'dashboard/student_profile.html')

def acads(request):
    return render(request, 'dashboard/acads_record.html')

#grade 7
def sectionOne(request):
    return render(request, 'dashboard/gradeseven/section_one.html')

def sectionTwo(request):
    return render(request, 'dashboard/gradeseven/section_two.html')

def sectionThree(request):
    return render(request, 'dashboard/gradeseven/section_three.html')

def sectionFour(request):
    return render(request, 'dashboard/gradeseven/section_four.html')

def sectionFive(request):
    return render(request, 'dashboard/gradeseven/section_five.html')


#grade 8
def eightsectionOne(request):
    return render(request, 'dashboard/gradeeight/eightsection_one.html')

def eightsectionTwo(request):
    return render(request, 'dashboard/gradeeight/eightsection_two.html')

def eightsectionThree(request):
    return render(request, 'dashboard/gradeeight/eightsection_three.html')

def eightsectionFour(request):
    return render(request, 'dashboard/gradeeight/eightsection_four.html')

def eightsectionFive(request):
    return render(request, 'dashboard/gradeeight/eightsection_five.html')


#grade 9
def ninesectionOne(request):
    return render(request, 'dashboard/gradenine/ninesection_one.html')

def ninesectionTwo(request):
    return render(request, 'dashboard/gradenine/ninesection_two.html')

def ninesectionThree(request):
    return render(request, 'dashboard/gradenine/ninesection_three.html')

def ninesectionFour(request):
    return render(request, 'dashboard/gradenine/ninesection_four.html')

def ninesectionFive(request):
    return render(request, 'dashboard/gradenine/ninesection_five.html')


#grade 10
def tensectionOne(request):
    return render(request, 'dashboard/gradeten/tensection_one.html')

def tensectionTwo(request):
    return render(request, 'dashboard/gradeten/tensection_two.html')

def tensectionThree(request):
    return render(request, 'dashboard/gradeten/tensection_three.html')

def tensectionFour(request):
    return render(request, 'dashboard/gradeten/tensection_four.html')

def tensectionFive(request):
    return render(request, 'dashboard/gradeten/tensection_five.html')