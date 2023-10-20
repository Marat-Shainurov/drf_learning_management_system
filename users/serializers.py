from datetime import datetime

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone', 'avatar', 'city', 'role')


class UserSerializer(serializers.ModelSerializer):
    last_login = SerializerMethodField()
    days_since_last_login = SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'avatar', 'city', 'role', 'last_login', 'days_since_last_login')

    @staticmethod
    def get_last_login(user):
        return user.last_login

    @staticmethod
    def get_days_since_last_login(user):
        if user.last_login:
            now = datetime.now()
            last_login = user.last_login.replace(tzinfo=None)
            diff = now - last_login
            return diff.days
        return
