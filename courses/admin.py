from django.contrib import admin

from courses.models import Course, Lesson, Subscription, Payment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_title', 'course_preview', 'user', 'price')
    list_filter = ('user',)
    search_fields = ('id', 'course_title')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson_title', 'lesson_preview', 'link_to_video', 'lesson_course', 'user', 'price')
    list_filter = ('user', 'lesson_course',)
    search_fields = ('id', 'lesson_title')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'course',)
    list_filter = ('course',)
    search_fields = ('id',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'payment_sum', 'payment_date', 'payment_type', 'paid_course', 'paid_lesson', 'payment_user',
        'payment_url', 'is_paid', 'payment_id',)
    list_filter = ('paid_course', 'paid_lesson', 'payment_user', 'is_paid')
    search_fields = ('id',)
