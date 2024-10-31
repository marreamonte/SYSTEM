# Generated by Django 4.2.16 on 2024-10-31 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0022_alter_studentprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='civil_status',
            field=models.CharField(choices=[('1', 'single'), ('2', 'married'), ('3', 'separated'), ('4', 'divorced'), ('5', 'widowed')], default='status', max_length=10, null=True),
        ),
    ]