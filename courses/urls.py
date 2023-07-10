from django.urls import path
from rest_framework.routers import DefaultRouter

from courses.apps import CoursesConfig
from courses.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonUpdateAPIView, \
    LessonDeleteAPIView, LessonRetrieveAPIView

app_name = CoursesConfig.name
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
  path('courses/lessons/create/', LessonCreateAPIView.as_view(), name='lessons_create'),
  path('courses/lessons/', LessonListAPIView.as_view(), name='lessons_list'),
  path('courses/lessons/detail/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lessons_detail'),
  path('courses/lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lessons_update'),
  path('courses/lessons/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lessons_delete'),
] + router.urls
