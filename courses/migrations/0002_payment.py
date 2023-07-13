# Generated by Django 4.2.3 on 2023-07-13 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_sum', models.PositiveIntegerField(verbose_name='payment_sum')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='payment_date')),
                ('payment_type', models.CharField(choices=[('cash', 'Cash'), ('transfer', 'Transfer')], max_length=10, verbose_name='payment_type')),
                ('paid_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course', verbose_name='paid_course')),
                ('paid_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.lesson', verbose_name='paid_course')),
                ('payment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='payment_user')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
