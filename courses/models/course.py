from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    course_title = models.CharField(verbose_name='course_title', max_length=250, unique=True)
    course_preview = models.ImageField(verbose_name='course_preview', upload_to='courses_previews', **NULLABLE)
    course_description = models.TextField(verbose_name='course_description', **NULLABLE)

    def __str__(self):
        return f'{self.course_title}'