from django.urls import path
from rest_framework.routers import DefaultRouter

from courses.apps import CoursesConfig
from courses.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonUpdateAPIView, \
    LessonDeleteAPIView, LessonRetrieveAPIView, PaymentRetrieveAPIView, PaymentCreateAPIView, PaymentListAPIView, \
    SubscriptionCreateAPIView, SubscriptionDestroyAPIView, SubscriptionListAPIView

app_name = CoursesConfig.name
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    # lessons urls
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lessons_create'),
    path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
    path('lessons/get/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lessons_detail'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lessons_update'),
    path('lessons/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lessons_delete'),

    # payments urls
    path('payments/create/', PaymentCreateAPIView.as_view(), name='payments_create'),
    path('payments/', PaymentListAPIView.as_view(), name='payments_list'),
    path('payments/detail/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payments_detail'),

    # subscriptions urls
    path('subscriptions/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscriptions/', SubscriptionListAPIView.as_view(), name='subscription_list'),
    path('subscriptions/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),
] + router.urls
