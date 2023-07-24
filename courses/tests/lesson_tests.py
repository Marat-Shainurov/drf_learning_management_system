from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson
from users.models import User, UserRoles


class LessonCRUDTestCases(APITestCase):
    def setUp(self):
        self.user_data = {'email': 'test@mail.com', "password": "123", "role": UserRoles.MODERATOR}
        self.user = User.objects.create(**self.user_data)
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(course_title="test course")

        self.lesson_data = {"lesson_title": "test lesson", "link_to_video": 'https://youtube.com/lesson/',
                            "lesson_course": self.course, "user": self.user}
        self.lesson = Lesson.objects.create(**self.lesson_data)

    def test_create_lesson(self):
        data = {"lesson_title": "test lesson 2", "link_to_video": 'https://youtube.com/lesson/2/',
                "lesson_course": self.course.id, "user": self.user.pk}
        response = self.client.post(reverse('courses:lessons_create'), data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.assertEquals(
            response.json(),
            {'id': 2, 'lesson_title': 'test lesson 2', 'lesson_description': None, 'lesson_preview': None,
             'link_to_video': 'https://youtube.com/lesson/2/', 'lesson_course': 1, 'user': 1}
        )

        self.assertEquals(Lesson.objects.all().count(), 2)

    def test_list_lesson(self):
        data = {"lesson_title": "test lesson 2", "link_to_video": 'https://youtube.com/lesson/2/',
                "lesson_course": self.course, "user": self.user}
        Lesson.objects.create(**data)

        response = self.client.get(reverse('courses:lessons_list'))
        print(response.json())

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(Lesson.objects.all().count(), 2)

    def test_update_lesson(self):
        data = {"lesson_title": "test lesson 2 - UPDATED", "link_to_video": 'https://youtube.com/lesson/2/',
                "lesson_course": self.course.id, "user": self.user.pk}
        response = self.client.put(reverse('courses:lessons_update', kwargs={"pk": 1}), data=data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            response.json(),
            {'id': 1, 'lesson_title': 'test lesson 2 - UPDATED', 'lesson_description': None, 'lesson_preview': None,
             'link_to_video': 'https://youtube.com/lesson/2/', 'lesson_course': 1, 'user': 1}
        )

    def test_partial_update_lesson(self):
        data = {"lesson_title": "test lesson 2 - UPDATED", 'link_to_video': 'https://youtube.com/lesson/new/'}
        response = self.client.patch(reverse('courses:lessons_update', kwargs={"pk": 1}), data=data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            response.json(),
            {'id': 1, 'lesson_title': 'test lesson 2 - UPDATED', 'lesson_description': None, 'lesson_preview': None,
             'link_to_video': 'https://youtube.com/lesson/new/', 'lesson_course': 1, 'user': 1}
        )

    def test_retrieve_lesson(self):
        response = self.client.get(reverse('courses:lessons_detail', kwargs={"pk": 1}))

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            response.json(),
            {'lesson_title': 'test lesson', 'lesson_description': None, 'lesson_preview': None,
             'link_to_video': 'https://youtube.com/lesson/', 'lesson_course': 'test course'}
        )

    def test_delete_lesson(self):
        response = self.client.delete(reverse('courses:lessons_delete', kwargs={"pk": 1}))

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEquals(Lesson.objects.all().count(), 0)
