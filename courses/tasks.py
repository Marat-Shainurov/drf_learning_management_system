from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

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
def set_pay_status(payment_id) -> None:
    """Sets True or False to the 'is_paid' field of the Payment model's objects depending on the payment status."""
    print(f"Payment status of {payment_id} -", get_payment_status(payment_id))
    if get_payment_status(payment_id):
        Payment.objects.get(pk=payment_id).is_paid = True
        print('Is paid!')
    print('Still unpaid')

