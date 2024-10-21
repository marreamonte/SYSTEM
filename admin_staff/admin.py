from django.contrib import admin
from .models import StudentProfile,Annoucement, AdminStaff, AdmissionStaff, FacultyStaff, GuidanceStaff, RegistrarStaff
# Register your models here.

admin.site.register(Annoucement)
admin.site.register(StudentProfile)
admin.site.register(AdminStaff)
admin.site.register(AdmissionStaff)
admin.site.register(FacultyStaff)
admin.site.register(GuidanceStaff)
admin.site.register(RegistrarStaff)