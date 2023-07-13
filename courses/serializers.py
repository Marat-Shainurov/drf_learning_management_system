from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from courses.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


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


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()

    class Meta:
        model = Course
        fields = ['course_title', 'lessons_count', 'lessons',]

    def get_lessons_count(self, course):
        return Lesson.objects.filter(lesson_course=course).count()

    def get_lessons(self, course):
        return LessonListSerializer(Lesson.objects.filter(lesson_course=course), many=True).data
