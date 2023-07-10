from django.contrib import admin

from courses.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_title',)
    list_filter = ('course_title',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_filter = ('lesson_title',)
