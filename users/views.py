from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from users.models import User
from users.serializers import UserSerializer


class UsersCreateAPIView(generics.CreateAPIView):
    """Creates new users."""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class UsersListAPIView(generics.ListAPIView):
    """Returns a list of users stored in the database."""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
