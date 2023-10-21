from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from courses.models import Subscription
from courses.paginators import MainPagination
from courses.serializers.subscription import SubscriptionSerializer


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """
    Creates a new Subscription object.
    """
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionListAPIView(generics.ListAPIView):
    """
    Returns a list of the Subscription model objects.
    """
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MainPagination


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    """
    Deletes Subscription objects.
    """
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]
