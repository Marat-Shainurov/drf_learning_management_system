from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class UsersCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UsersListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UsersRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UsersUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
