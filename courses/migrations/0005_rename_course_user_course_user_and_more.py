# Generated by Django 4.2.3 on 2023-07-18 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_course_user_lesson_lesson_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='lesson_user',
            new_name='user',
        ),
    ]
