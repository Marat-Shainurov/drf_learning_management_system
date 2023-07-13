# Generated by Django 4.2.3 on 2023-07-13 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paid_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course', to='courses.course', verbose_name='paid_course'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paid_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson', to='courses.lesson', verbose_name='paid_course'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='payment_user'),
        ),
    ]