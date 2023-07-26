from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from courses.models import Lesson
from courses.paginators import MainPagination
from courses.serializers import LessonSerializer, LessonDetailSerializer
from courses.permissions import IsOwner, IsModerator


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Creates a new Lesson object, assigning self.request.user as the object's user.
    APIView's serializer - LessonSerializer.
    """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """
    Returns a list of Lesson objects, with MainPagination pagination settings.
    The list is filtered by user=self.request.user.
    APIView's serializer - LessonSerializer.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MainPagination

    def get_queryset(self):
        user = self.request.user
        return Lesson.objects.filter(user=user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Returns a Lesson object.
    APIView's serializer - LessonDetailSerializer.
    """
    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Updates the Lesson model's object.
    APIView's serializer - LessonSerializer.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonDeleteAPIView(generics.DestroyAPIView):
    """
    Deletes the Lesson model's object.
    APIView's serializer - LessonSerializer.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]
