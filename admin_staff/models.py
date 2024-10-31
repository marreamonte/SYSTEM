from django.db import models

# Create your models here.

class section(models.Model):
    section_name = models.CharField(max_length=20);

class level(models.Model):
    level = models.CharField(max_length=20);


class Announcement(models.Model):
    announcement_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    event = models.DateField(null=True)

    class Meta:
        managed = True
        db_table = 'annoucement'
    
    def __str__(self):
        return self.title


class StudentProfile(models.Model):
    student_lrn = models.BigIntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    section = models.CharField(max_length=24)
    gender = models.CharField(max_length=24, blank=True, null=True)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=24, blank=True, null=True)
    civil_status = models.CharField(max_length=10, null=True)
    contact = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student_profile'
    
    def __str__(self):
        return str(self.student_lrn)
    
class AdminStaff(models.Model):
    admin_staff_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    gender = models.CharField(max_length=24, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_staff'


class AdmissionStaff(models.Model):
    admission_staff_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    gender = models.CharField(max_length=24, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admission_staff'


class FacultyStaff(models.Model):
    faculty_staff_id = models.BigIntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    section = models.CharField(max_length=24)
    gender = models.CharField(max_length=24, blank=True, null=True)
    contact = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'faculty_staff'

    def __str__(self):
        return str(self.faculty_staff_id)


class GuidanceStaff(models.Model):
    guidance_staff_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    gender = models.CharField(max_length=24, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guidance_staff'


class RegistrarStaff(models.Model):
    registrar_staff_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    gender = models.CharField(max_length=24, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registrar_staff'