from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from users.models import User
from lms.models import Course, Lesson, Subscription


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@email.ru')
        self.lesson = Lesson.objects.create(title='test_lesson', description='test', owner=self.user)
        self.course = Course.objects.create(title='test_course', description='test', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        url = reverse('lms:lesson_create')
        data = {
            'title': 'Кексы',
            'description': 'Тестим кексы',
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse('lms:lesson_update', args=(self.lesson.pk,))
        data = {
            'title': 'Кексы(2)',
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), 'Кексы(2)')

    def test_lesson_retrieve(self):
        url = reverse('lms:lesson_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_destroy(self):
        url = reverse('lms:lesson_destroy', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_lesson_list(self):
        url = reverse('lms:lesson_list')
        response = self.client.get(url)
        data = response.json()
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [{'id': self.lesson.pk,
                               'title': self.lesson.title,
                               'description': self.lesson.description,
                               'preview': None,
                               'video': None,
                               'course': self.lesson.course,
                               'owner': self.lesson.owner.pk}
                              ]
                  }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@email.ru')
        self.course = Course.objects.create(title='test_course', description='test', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        url = reverse('lms:subscription_create')
        data = {
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.all().count(), 1)
        self.assertEqual(response.json(), {'massage': 'Подписка создана'})

    def test_subscription_delete(self):
        url = reverse('lms:subscription_create')
        data = {
            'course': self.course.pk
        }
        self.client.post(url, data)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.all().count(), 0)
        self.assertEqual(response.json(), {'massage': 'Подписка удалена'})
