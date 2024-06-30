from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from lms.models import Course, Lesson
from lms.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerator, IsOwner

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'list', 'retrieve']:
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        if self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, ~IsModerator | IsOwner]
        return super().get_permissions()


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator | IsOwner]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerator | IsOwner]
