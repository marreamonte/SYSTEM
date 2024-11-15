# Generated by Django 5.1.3 on 2024-11-14 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0004_remove_facultystaff_subject_delete_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectname', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='facultystaff',
            name='subject',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_staff.subject'),
        ),
    ]
