# Generated by Django 3.2.9 on 2021-11-27 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0002_student_studentunion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentunion',
            name='unionRoot',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='studentUnion',
        ),
    ]
