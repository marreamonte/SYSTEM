from django.contrib import admin
from .models import StudentProfile,Announcement, FacultyStaff, AdminStaff, AdmissionStaff, GuidanceStaff, RegistrarStaff, section, level, UserAccount

# Register your models here.

@admin.register(StudentProfile)
class students(admin.ModelAdmin):
    list_display = ('student_lrn', 'surname', 'first_name', 'section')
    ordering = ('student_lrn', )
    search_fields = ('surname', 'student_lrn')


@admin.register(FacultyStaff)
class faculty(admin.ModelAdmin):
    list_display = ('faculty_staff_id', 'surname', 'first_name', 'section')
    ordering = ('faculty_staff_id', )
    search_fields = ('surname', 'faculty_staff_id')
admin.site.register(section)



@admin.register(UserAccount)
class students(admin.ModelAdmin):
    list_display = ('user', 'username', 'passcode')
    
@admin.register(level)
class level(admin.ModelAdmin):
    list_display = ('level',  )
    ordering = ('level', )


    


@admin.register(Announcement)
class announcement(admin.ModelAdmin):
    list_display = ('title', 'event')
    ordering = ('title', )
    search_fields = ('title', )










admin.site.register(AdminStaff)
admin.site.register(AdmissionStaff)


admin.site.register(GuidanceStaff)
admin.site.register(RegistrarStaff)