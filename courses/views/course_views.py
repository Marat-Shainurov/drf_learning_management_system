from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from courses.models import Course
from courses.permissions import IsModerator, IsOwner
from courses.serializers import CourseSerializer, CourseDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    default_serializer = CourseSerializer
    queryset = Course.objects.all()
    serializers = {
        'retrieve': CourseDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        user = self.request.user
        queryset = self.filter_queryset(self.get_queryset().filter(user=user))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            permission_classes = [IsAuthenticated, IsModerator]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

