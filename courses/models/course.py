from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    course_title = models.CharField(verbose_name='course_title', max_length=250, unique=True)
    course_preview = models.ImageField(verbose_name='course_preview', upload_to='courses_previews', **NULLABLE)
    course_description = models.TextField(verbose_name='course_description', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='course_user', **NULLABLE)
    price = models.PositiveIntegerField(default=0, verbose_name='course_price')

    def __str__(self):
        return f'{self.course_title}'

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
