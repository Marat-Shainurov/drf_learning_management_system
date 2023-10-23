from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class CustomUserTestCase(APITestCase):

    def setUp(self):
        data_user = {'email': 'test@mail.com', 'password': 123, 'city': 'LA', 'is_staff': True, 'phone': '+79998336868'}
        self.test_user = User.objects.create(**data_user)
        self.client.force_authenticate(user=self.test_user)

    def test_create_user(self):
        data_user = {'email': 't2@mail.com', 'password': 123, 'city': 'LA', 'is_staff': True, 'phone': '+79998337777'}
        response = self.client.post('http://localhost:8000/users/create/', data=data_user)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json()['email'], data_user['email'])
        self.assertEquals(response.json()['city'], data_user['city'])
        self.assertEquals(response.json()['phone'], data_user['phone'])
        self.assertEquals(response.json()['role'], 'member')
        self.assertEquals(response.json()['avatar'], None)

    def test_create_user_invalid_data(self):
        data_user_invalid_email = {'email': 'wrong.com', 'password': 'qweasd123qwe'}
        response_invalid_email = self.client.post('http://localhost:8000/users/create/', data=data_user_invalid_email)
        self.assertEquals(response_invalid_email.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response_invalid_email.json()['email'], ['Enter a valid email address.'])

        data_user_not_unique = {'email': 'test@mail.com', 'password': 'qweasd123qwe'}
        response_not_unique = self.client.post('http://localhost:8000/users/create/', data=data_user_not_unique)
        self.assertEquals(response_not_unique.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response_not_unique.json()['email'], ['user with this user_email already exists.'])

        data_user_invalid_role = {'email': 'm_shainurov@mail.com', 'password': 'qweasd123qwe', 'role': 'invalid'}
        response_invalid_role = self.client.post('http://localhost:8000/users/create/', data=data_user_invalid_role)
        self.assertEquals(response_invalid_role.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response_invalid_role.json()['role'], ['"invalid" is not a valid choice.'])

    def test_list_users(self):
        data_user = {'email': 'test_two@mail.com', 'password': 'qweasd123qwe'}
        self.client.post('http://localhost:8000/users/create/', data=data_user)
        response_get = self.client.get('http://localhost:8000/users/')
        self.assertEquals(response_get.status_code, status.HTTP_200_OK)
        self.assertEquals(User.objects.all().count(), 2)
        self.assertEquals(response_get.json()['results'][0]['email'], self.test_user.email)
        self.assertEquals(response_get.json()['results'][1]['email'], data_user['email'])
