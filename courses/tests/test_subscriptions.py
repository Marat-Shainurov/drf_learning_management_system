from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Subscription
from users.models import User, UserRoles


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user_data = {'email': 'test_email@mail.com', "password": "123", "role": UserRoles.MODERATOR}
        self.user = User.objects.create(**self.user_data)
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(course_title="test course")

    def test_create_subscription(self):
        subscription_data = {'user': self.user.pk, 'course': self.course.pk}
        response = self.client.post(reverse('courses:subscription_create'), data=subscription_data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json(), {'id': 1, 'user': self.user.pk, 'course': self.course.pk})

    def test_delete_subscription(self):
        subscription = Subscription.objects.create(user=self.user, course=self.course)
        response = self.client.delete(reverse('courses:subscription_delete', kwargs={"pk": subscription.pk}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Subscription.objects.all().count(), 0)

    def test_list_subscriptions(self):
        subscription = Subscription.objects.create(user=self.user, course=self.course)
        response = self.client.get(reverse('courses:subscription_list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(isinstance(response.json()['results'], list), True)
        self.assertEquals(
            response.json()['results'][0],
            {'course': self.course.pk, 'id': subscription.pk, 'user': self.user.pk})
