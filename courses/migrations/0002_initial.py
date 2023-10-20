# Generated by Django 4.2.3 on 2023-10-20 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribed_user', to=settings.AUTH_USER_MODEL, verbose_name='subscribed_user'),
        ),
        migrations.AddField(
            model_name='payment',
            name='paid_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course', to='courses.course', verbose_name='paid_course'),
        ),
        migrations.AddField(
            model_name='payment',
            name='paid_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson', to='courses.lesson', verbose_name='paid_lesson'),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='payment_user'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_course', to='courses.course', verbose_name='lesson_course'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='lesson_user'),
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='course_user'),
        ),
    ]
