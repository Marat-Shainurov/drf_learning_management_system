import json
from datetime import timedelta, datetime

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from courses.models import Subscription, Course, Payment
from courses.services import get_payment_status


@shared_task
def inform_subscribers_course_upd(course_pk):
    updated_course = Course.objects.get(pk=course_pk)
    subscribers = [subscription.user.email for subscription in Subscription.objects.filter(course=updated_course)]

    send_mail(
        subject=f'{updated_course.course_title} course update',
        message=f'{updated_course.course_title} has been updated!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=subscribers,
    )


@shared_task
def set_pay_status(payment_pk: str) -> None:
    """Sets True or False to the 'is_paid' field of the Payment model's objects depending on the payment status."""
    if get_payment_status(payment_pk):
        payment_obj = get_object_or_404(Payment, pk=payment_pk)
        payment_obj.is_paid = True
        payment_obj.save()


def set_pay_status_schedule(payment_pk) -> None:
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.MINUTES,
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name=f'Set payment status for the "{payment_pk}" payment',
        task='courses.tasks.set_pay_status',
        args=json.dumps([payment_pk, ]),
        kwargs={},
        expires=datetime.utcnow() + timedelta(minutes=10)
    )
