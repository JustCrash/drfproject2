from rest_framework.serializers import ModelSerializer, SerializerMethodField
from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, object):
        if object.lesson_set.count():
            return object.lesson_set.count()
        return 0


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
