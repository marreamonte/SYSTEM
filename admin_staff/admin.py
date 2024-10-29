from django.contrib import admin
from .models import StudentProfile,Annoucement, AdminStaff, AdmissionStaff, FacultyStaff, GuidanceStaff, RegistrarStaff, section, level
# Register your models here.

@admin.register(level)
class level(admin.ModelAdmin):
    list_display = ('level',  )
    ordering = ('level', )

@admin.register(section)
class section(admin.ModelAdmin):
    list_display = ('section_name', )


@admin.register(Annoucement)
class announcement(admin.ModelAdmin):
    list_display = ('title', 'event')
    ordering = ('title', )
    search_fields = ('title', )



@admin.register(StudentProfile)
class students(admin.ModelAdmin):
    list_display = ('student_lrn', 'surname', 'first_name', 'section')
    ordering = ('student_lrn', )
    search_fields = ('surname', 'student_lrn')


admin.site.register(AdminStaff)
admin.site.register(AdmissionStaff)


@admin.register(FacultyStaff)
class faculty(admin.ModelAdmin):
    list_display = ('faculty_staff_id', 'surname', 'first_name', 'section')
    ordering = ('faculty_staff_id',)
    search_fields = ('surname', 'faculty_staff_id')





admin.site.register(GuidanceStaff)
admin.site.register(RegistrarStaff)