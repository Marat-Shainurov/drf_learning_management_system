from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from courses.models import Course
from courses.paginators import MainPagination
from courses.permissions import IsModerator, IsOwner
from courses.serializers import CourseDetailSerializer, CourseCreateUpdateSerializer
from courses.tasks import inform_subscribers_course_upd


class CourseViewSet(viewsets.ModelViewSet):
    """ ViewSet for the Course model """
    queryset = Course.objects.all()
    pagination_class = MainPagination

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT', 'PATCH'):
            return CourseCreateUpdateSerializer
        else:
            return CourseDetailSerializer

    def perform_create(self, serializer):
        new_data = serializer.save()
        new_data.user = self.request.user
        new_data.save()

    def perform_update(self, serializer):
        new_data = serializer.save()
        new_data.save()
        inform_subscribers_course_upd.delay(new_data.pk)

    def list(self, request, *args, **kwargs):
        """ Returns a list of courses, with MainPagination pagination settings """
        user = self.request.user
        queryset = self.filter_queryset(self.get_queryset().filter(user=user))
        serializer = self.get_serializer(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            permission_classes = [IsAuthenticated, IsModerator]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
