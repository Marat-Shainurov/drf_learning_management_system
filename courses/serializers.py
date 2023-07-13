from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from courses.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()

    class Meta:
        model = Course
        fields = ('course_title', 'lessons_count')

    def get_lessons_count(self, course):
        return Lesson.objects.filter(lesson_course=course).count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonDetailSerializer(serializers.ModelSerializer):
    lesson_course = SlugRelatedField(slug_field='course_title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = (
        'lesson_title', 'lesson_description', 'lesson_preview', 'link_to_video', 'lesson_course',
        )
