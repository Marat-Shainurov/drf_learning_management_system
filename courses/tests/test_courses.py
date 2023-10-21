from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course
from users.models import User, UserRoles


class CoursesTestCase(APITestCase):

    def setUp(self) -> None:
        self.user_data = {'email': 'test@mail.com', "password": "123", "role": UserRoles.MODERATOR}
        self.user = User.objects.create(**self.user_data)
        self.client.force_authenticate(user=self.user)
        self.course_data = {"course_title": "Test Course", "price": 30000}
        self.test_course = Course.objects.create(**self.course_data)

    def test_create_course(self):
        course_data = {"course_title": "Test Course Create", "price": 50000}
        response = self.client.post('https://localhost/courses/', data=course_data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json()['course_title'], course_data['course_title'])
        self.assertEquals(response.json()['price'], course_data['price'])

    def test_retrieve_course(self):
        response = self.client.get(f'https://localhost/courses/{self.test_course.pk}/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['id'], self.test_course.pk)
        self.assertEquals(response.json()['course_title'], self.test_course.course_title)
        self.assertEquals(response.json()['price'], self.test_course.price)

        invalid_response = self.client.get(f'https://localhost/courses/1000/')
        self.assertEquals(invalid_response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(invalid_response.json(), {'detail': 'Not found.'})

    def test_update_course(self):
        data_to_update = {'course_title': 'UPDATED', 'price': 2000}
        response = self.client.put(f'https://localhost/courses/{self.test_course.pk}/', data=data_to_update)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['course_title'], data_to_update['course_title'])
        self.assertEquals(response.json()['price'], data_to_update['price'])
        updated_obj = get_object_or_404(Course, pk=self.test_course.pk)
        self.assertEquals(updated_obj.course_title, data_to_update['course_title'])
        self.assertEquals(updated_obj.price, data_to_update['price'])

        invalid_response = self.client.put(f'https://localhost/courses/{self.test_course.pk}/', data={'price': 1000})
        self.assertEquals(invalid_response.json(), {'course_title': ['This field is required.']})

    def test_partial_update_price(self):
        data_to_update_price = {'price': 60000}
        response_price = self.client.patch(
            f'https://localhost/courses/{self.test_course.pk}/', data=data_to_update_price)
        self.assertEquals(response_price.status_code, status.HTTP_200_OK)
        self.assertEquals(response_price.json()['course_title'], self.test_course.course_title)
        self.assertEquals(response_price.json()['price'], data_to_update_price['price'])

    def test_partial_update_title(self):
        data_to_update_title = {'course_title': 'Partially Updated'}
        response_title = self.client.patch(
            f'https://localhost/courses/{self.test_course.pk}/', data=data_to_update_title)
        self.assertEquals(response_title.status_code, status.HTTP_200_OK)
        self.assertEquals(response_title.json()['price'], self.test_course.price)
        self.assertEquals(response_title.json()['course_title'], data_to_update_title['course_title'])

    def test_delete_course(self):
        stored_courses = Course.objects.filter(pk=self.test_course.pk)
        self.assertEquals(stored_courses.exists(), True)
        response = self.client.delete(f'https://localhost/courses/{self.test_course.pk}/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        stored_courses = Course.objects.filter(pk=self.test_course.pk)
        self.assertEquals(stored_courses.exists(), False)
