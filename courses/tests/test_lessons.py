from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson
from users.models import User, UserRoles


class LessonTestCases(APITestCase):
    def setUp(self):
        self.user_data = {'email': 'test@mail.com', "password": "123", "role": UserRoles.MODERATOR}
        self.user = User.objects.create(**self.user_data)
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(course_title="test course")
        self.lesson_data = {"lesson_title": "test lesson", "link_to_video": 'https://youtube.com/test-lesson/',
                            "lesson_course": self.course, "user": self.user}
        self.test_lesson = Lesson.objects.create(**self.lesson_data)

    def test_create_lesson(self):
        data = {"lesson_title": "test lesson create", "link_to_video": 'https://youtube.com/lesson-create/',
                "lesson_course": self.course.id, "user": self.user.pk}
        response = self.client.post(reverse('courses:lessons_create'), data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json()['lesson_title'], data['lesson_title'])
        self.assertEquals(response.json()['lesson_title'], data['lesson_title'])
        self.assertEquals(response.json()['link_to_video'], data['link_to_video'])
        self.assertEquals(response.json()['price'], 0)
        self.assertEquals(Lesson.objects.all().count(), 2)

    def test_list_lesson(self):
        response = self.client.get(reverse('courses:lessons_list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Lesson.objects.all().count(), 1)
        self.assertEquals(isinstance(response.json()['results'], list), True)
        self.assertEquals(response.json()['results'][0]['id'], self.test_lesson.pk)
        self.assertEquals(response.json()['results'][0]['lesson_title'], self.test_lesson.lesson_title)

    def test_update_lesson(self):
        stored_lesson = get_object_or_404(Lesson, pk=self.test_lesson.pk)
        self.assertEquals(stored_lesson.lesson_title, self.lesson_data['lesson_title'])

        data_to_update = {"lesson_title": "UPDATED", "link_to_video": 'https://youtube.com/lesson/2/',
                          "lesson_course": self.course.pk, "user": self.user.pk}
        response = self.client.put(reverse(
            'courses:lessons_update', kwargs={"pk": self.test_lesson.pk}), data=data_to_update)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['lesson_title'], data_to_update['lesson_title'])
        self.assertEquals(response.json()['link_to_video'], data_to_update['link_to_video'])

        stored_lesson_updated = get_object_or_404(Lesson, pk=self.test_lesson.pk)
        self.assertEquals(stored_lesson_updated.lesson_title, data_to_update['lesson_title'])
        self.assertEquals(stored_lesson_updated.link_to_video, data_to_update['link_to_video'])

    def test_partial_update_lesson_title(self):
        stored_lesson = get_object_or_404(Lesson, pk=self.test_lesson.pk)
        self.assertEquals(stored_lesson.lesson_title, self.lesson_data['lesson_title'])

        data_to_update = {"lesson_title": "UPDATED"}
        response = self.client.patch(reverse(
            'courses:lessons_update', kwargs={"pk": self.test_lesson.pk}), data=data_to_update)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['lesson_title'], data_to_update['lesson_title'])
        self.assertEquals(response.json()['link_to_video'], self.test_lesson.link_to_video)

        stored_lesson_updated = get_object_or_404(Lesson, pk=self.test_lesson.pk)
        self.assertEquals(stored_lesson_updated.lesson_title, data_to_update['lesson_title'])
        self.assertEquals(stored_lesson_updated.link_to_video, self.test_lesson.link_to_video)

    def test_retrieve_lesson(self):
        response = self.client.get(reverse('courses:lessons_detail', kwargs={"pk": self.test_lesson.pk}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['lesson_title'], self.test_lesson.lesson_title)
        self.assertEquals(response.json()['id'], self.test_lesson.pk)
        self.assertEquals(response.json()['price'], self.test_lesson.price)
        self.assertEquals(response.json()['lesson_preview'], self.test_lesson.lesson_preview)
        self.assertEquals(response.json()['link_to_video'], self.test_lesson.link_to_video)
        self.assertEquals(response.json()['lesson_course'], str(self.test_lesson.lesson_course))
        self.assertEquals(response.json()['user'], self.test_lesson.user.pk)

    def test_delete_lesson(self):
        stored_lesson = Lesson.objects.filter(pk=self.test_lesson.pk)
        self.assertEquals(stored_lesson.exists(), True)
        response = self.client.delete(reverse('courses:lessons_delete', kwargs={"pk": self.test_lesson.pk}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        stored_lesson = Lesson.objects.filter(pk=self.test_lesson.pk)
        self.assertEquals(stored_lesson.exists(), False)

