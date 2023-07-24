from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from courses.models import Course, Lesson, Subscription
from courses.serializers.lesson_serializers import LessonListSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonListSerializer(source='lesson_course', many=True)
    is_user_subscribed = SerializerMethodField()

    class Meta:
        model = Course
        fields = ['course_title', 'lessons_count', 'lessons', 'is_user_subscribed', 'user', 'price']

    def get_lessons_count(self, course):
        return Lesson.objects.filter(lesson_course=course).count()

    def get_is_user_subscribed(self, course):
        subscriptions = Subscription.objects.all()
        return subscriptions.filter(user=course.user).exists()
