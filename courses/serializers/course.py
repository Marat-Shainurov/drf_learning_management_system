from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from courses.models import Course, Lesson, Subscription
from courses.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'course_title', 'price')


class CourseCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_title', 'course_preview', 'course_description', 'price')


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(source='lesson_course', many=True)
    is_user_subscribed = SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'course_title', 'lessons_count', 'lessons', 'is_user_subscribed', 'user', 'price']

    @staticmethod
    def get_lessons_count(course):
        return Lesson.objects.filter(lesson_course=course).count()

    @staticmethod
    def get_is_user_subscribed(course):
        return Subscription.objects.filter(user=course.user).exists()
