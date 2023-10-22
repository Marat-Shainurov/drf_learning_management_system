from django.db import models
from rest_framework.exceptions import ValidationError

from courses.models import Course, Lesson
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):
    PAYMENT_TYPE_CHOICE = [
        ('cash', 'Cash'),
        ('transfer', 'Transfer')
    ]

    payment_sum = models.PositiveIntegerField(verbose_name='payment_sum', **NULLABLE)
    payment_date = models.DateTimeField(verbose_name='payment_date', auto_now_add=True)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE_CHOICE, verbose_name='payment_type')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='paid_course',
                                    related_name='paid_courses', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='paid_lesson',
                                    related_name='paid_lessons', **NULLABLE)
    payment_user = models.ForeignKey(User, verbose_name='payment_user', related_name='user_payments',
                                     on_delete=models.SET_NULL, **NULLABLE)
    payment_url = models.URLField(verbose_name='payment_url', max_length=500, **NULLABLE)
    is_paid = models.BooleanField(verbose_name='payment_status', default=False)
    payment_id = models.CharField(verbose_name='payment_id', max_length=250, **NULLABLE)

    def __str__(self):
        return f'{self.payment_user}, {self.paid_lesson if self.paid_lesson else self.paid_course}, {self.payment_sum}'

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def clean(self):
        if self.paid_lesson and self.paid_course:
            raise ValidationError("Either paid_course or paid_lesson must be selected. You have selected both.")
        if not self.paid_course and not self.paid_lesson:
            raise ValidationError("Neither paid_course nor paid_lesson are selected.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
