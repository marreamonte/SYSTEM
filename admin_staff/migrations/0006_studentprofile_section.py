# Generated by Django 4.2.16 on 2024-10-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0005_alter_studentprofile_student_lrn'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='section',
            field=models.CharField(blank=True, max_length=24),
        ),
    ]