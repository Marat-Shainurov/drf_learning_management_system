from django.urls import path
from rest_framework.routers import DefaultRouter

from courses.apps import CoursesConfig
from courses.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonUpdateAPIView, \
    LessonDeleteAPIView, LessonRetrieveAPIView, PaymentRetrieveAPIView, PaymentCreateAPIView, PaymentListAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView

app_name = CoursesConfig.name
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [

    # lessons urls
    path('courses/lessons/create/', LessonCreateAPIView.as_view(), name='lessons_create'),
    path('courses/lessons/', LessonListAPIView.as_view(), name='lessons_list'),
    path('courses/lessons/detail/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lessons_detail'),
    path('courses/lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lessons_update'),
    path('courses/lessons/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lessons_delete'),

    # payments urls
    path('courses/payments/create/', PaymentCreateAPIView.as_view(), name='payments_create'),
    path('courses/payments/', PaymentListAPIView.as_view(), name='payments_list'),
    path('courses/payments/detail/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payments_detail'),

    # subscriptions urls
    path('courses/subscriptions/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('courses/subscriptions/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),

] + router.urls
