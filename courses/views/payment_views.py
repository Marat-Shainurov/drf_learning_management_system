from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.management import call_command
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import generics

from courses.models import Payment
from courses.serializers import PaymentSerializer, PaymentCreateSerializer
import stripe

from courses.services import create_product, create_price, create_payment, set_pay_status_schedule


class PaymentCreateAPIView(generics.CreateAPIView):
    """
    Creates a new Payment object, assigning self.request.user as the object's user.
    Launches payment status tracking (the 'is_paid' field), via a periodic celery task.
    APIView's serializer - PaymentCreateSerializer.
    """
    serializer_class = PaymentCreateSerializer

    def perform_create(self, serializer):
        new_payment = serializer.save()

        if not new_payment.paid_course and not new_payment.paid_lesson:
            raise ValidationError("Either paid_course or paid_lesson must be selected.")

        new_payment.payment_user = self.request.user
        new_payment.payment_sum = new_payment.paid_course.price if new_payment.paid_course else new_payment.paid_lesson.price
        new_payment_product = new_payment.paid_course if new_payment.paid_course else new_payment.paid_lesson
        new_payment.save()

        if new_payment.payment_type == 'cash':
            new_payment.is_paid = True
            new_payment.save()
        else:
            stripe.api_key = settings.STRIPE_API_KEY
            product = create_product(new_payment_product)
            price = create_price(new_payment, product)
            payment = create_payment(price)

            new_payment.payment_url = payment['url']
            new_payment.payment_id = payment['id']
            new_payment.save()

        set_pay_status_schedule(new_payment.pk)

class PaymentListAPIView(generics.ListAPIView):
    """
    Returns a list of payments.
    APIView's serializer - PaymentSerializer.
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_type',)
    ordering_fields = ('payment_date',)


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    """
    Returns the Payment model's object.
    APIView's serializer - PaymentSerializer.
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
