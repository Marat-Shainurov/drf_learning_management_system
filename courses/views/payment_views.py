from django.core.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import generics

from courses.models import Payment
from courses.serializers import PaymentSerializer, PaymentCreateSerializer
import stripe


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializer

    def perform_create(self, serializer):
        new_payment = serializer.save()

        if not new_payment.paid_course and not new_payment.paid_lesson:
            raise ValidationError("Either paid_course or paid_lesson must be selected.")

        new_payment.user = self.request.user
        new_payment.payment_sum = new_payment.paid_course.price if new_payment.paid_course else new_payment.paid_lesson.price
        new_payment.save()

        stripe.api_key = "sk_test_51NXmWXJiDDtWvXOb6yqZ6UDCLLz8kr1wtRVVqMeyDHSL0oIQYlLhUjHDOwKlInBUuUACFQ6zcyO3IhzZTFPfYvM300KGnycyF7"
        stripe.PaymentIntent.create(
            amount=new_payment.payment_sum,
            currency="rub",
            automatic_payment_methods={"enabled": True},
        )


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_type',)
    ordering_fields = ('payment_date',)


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
