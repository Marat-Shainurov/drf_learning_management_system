from django.conf import settings
from django.db import models

from courses.models import Course
from users.models import NULLABLE


class Lesson(models.Model):
    lesson_title = models.CharField(verbose_name='lesson_title', max_length=250)
    lesson_description = models.TextField(verbose_name='lesson_description', **NULLABLE)
    lesson_preview = models.ImageField(verbose_name='lesson_preview', upload_to='lessons_previews', **NULLABLE)
    link_to_video = models.URLField(verbose_name='link_to_lesson_video', max_length=250, **NULLABLE)
    lesson_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson_course',
                                      verbose_name='lesson_course')
    lesson_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='lesson_user',
                                    **NULLABLE)

    def __str__(self):
        return f'{self.lesson_title}'
