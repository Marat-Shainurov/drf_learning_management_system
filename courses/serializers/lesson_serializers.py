from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from courses.models import Lesson, Course
from courses.validators import LinkValidator


class LessonCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'lesson_title', 'lesson_description', 'lesson_preview', 'link_to_video', 'lesson_course', 'user', 'price')
        validators = [LinkValidator(field='link_to_video')]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'id', 'lesson_title', 'link_to_video', 'user', 'price',)
        validators = [LinkValidator(field='link_to_video')]


class LessonDetailSerializer(serializers.ModelSerializer):
    lesson_course = SlugRelatedField(slug_field='course_title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = (
            'id', 'lesson_title', 'lesson_description', 'lesson_preview', 'link_to_video', 'lesson_course', 'user',
            'price',)
