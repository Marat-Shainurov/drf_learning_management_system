from django.db import models

from courses.models import Course, Lesson
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):

    PAYMENT_TYPE_CHOICE = [
        ('cash', 'Cash'),
        ('transfer', 'Transfer')
    ]

    payment_sum = models.PositiveIntegerField(verbose_name='payment_sum')
    payment_date = models.DateTimeField(verbose_name='payment_date', auto_now_add=True)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE_CHOICE, verbose_name='payment_type')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='paid_course', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='paid_course', **NULLABLE)
    payment_user = models.ForeignKey(User, verbose_name='payment_user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.payment_user}, {self.paid_lesson if self.paid_lesson else self.paid_course}, {self.payment_sum}'

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
