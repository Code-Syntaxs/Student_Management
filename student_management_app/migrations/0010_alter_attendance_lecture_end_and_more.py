# Generated by Django 5.1.5 on 2025-01-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0009_attendance_lecture_end_attendance_lecture_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='lecture_end',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='lecture_start',
            field=models.TimeField(),
        ),
    ]
