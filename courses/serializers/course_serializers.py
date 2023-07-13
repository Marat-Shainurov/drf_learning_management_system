from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from courses.models import Course, Lesson
from courses.serializers.lesson_serializers import LessonListSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()

    class Meta:
        model = Course
        fields = ['course_title', 'lessons_count', 'lessons', ]

    def get_lessons_count(self, course):
        return Lesson.objects.filter(lesson_course=course).count()

    def get_lessons(self, course):
        return LessonListSerializer(Lesson.objects.filter(lesson_course=course), many=True).data
