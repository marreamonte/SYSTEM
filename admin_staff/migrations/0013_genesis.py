# Generated by Django 4.2.16 on 2024-10-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0012_alter_facultystaff_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adviserSurname', models.CharField(max_length=24)),
            ],
        ),
    ]
