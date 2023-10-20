# Generated by Django 4.2.3 on 2023-10-20 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=250, unique=True, verbose_name='course_title')),
                ('course_preview', models.ImageField(blank=True, null=True, upload_to='courses_previews', verbose_name='course_preview')),
                ('course_description', models.TextField(blank=True, null=True, verbose_name='course_description')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='course_price')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_title', models.CharField(max_length=250, verbose_name='lesson_title')),
                ('lesson_description', models.TextField(blank=True, null=True, verbose_name='lesson_description')),
                ('lesson_preview', models.ImageField(blank=True, null=True, upload_to='lessons_previews', verbose_name='lesson_preview')),
                ('link_to_video', models.URLField(blank=True, max_length=250, null=True, verbose_name='link_to_lesson_video')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='lesson_price')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_sum', models.PositiveIntegerField(blank=True, null=True, verbose_name='payment_sum')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='payment_date')),
                ('payment_type', models.CharField(choices=[('cash', 'Cash'), ('transfer', 'Transfer')], max_length=10, verbose_name='payment_type')),
                ('payment_url', models.URLField(blank=True, max_length=500, null=True, verbose_name='payment_url')),
                ('is_paid', models.BooleanField(default=False, verbose_name='payment_status')),
                ('payment_id', models.CharField(blank=True, max_length=250, null=True, verbose_name='payment_id')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_course', to='courses.course', verbose_name='subscription_course')),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
            },
        ),
    ]
