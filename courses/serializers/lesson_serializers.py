from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from courses.models import Lesson, Course
from courses.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link_to_video')]


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['lesson_title', 'lesson_description', 'link_to_video']


class LessonDetailSerializer(serializers.ModelSerializer):
    lesson_course = SlugRelatedField(slug_field='course_title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = (
            'lesson_title', 'lesson_description', 'lesson_preview', 'link_to_video', 'lesson_course',
        )
