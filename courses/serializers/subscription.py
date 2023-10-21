from rest_framework import serializers

from courses.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class SubscriptionSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id', 'course',)
