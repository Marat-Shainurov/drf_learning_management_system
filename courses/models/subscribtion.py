from django.conf import settings
from django.db import models

from courses.models import Course


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='subscribed_user', on_delete=models.CASCADE,
                             related_name='user_subscriptions')
    course = models.ForeignKey(Course, verbose_name='subscription_course', on_delete=models.CASCADE,
                               related_name='course_subscriptions')

    def __str__(self):
        return f'{self.user} subscribed to {self.course}'

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'


