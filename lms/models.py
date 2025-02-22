from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='название', help_text='Введите название')
    preview = models.ImageField(upload_to='course_preview/', **NULLABLE, help_text='Вставъте превью')
    description = models.TextField(max_length=250, verbose_name='описание', **NULLABLE, help_text='Введите описание')
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name='Стоимость курса', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='название', help_text='Введите название')
    description = models.TextField(max_length=250, verbose_name='описание', **NULLABLE, help_text='Введите описание')
    preview = models.ImageField(upload_to='lesson_preview/', **NULLABLE, help_text='Вставъте превью')
    video = models.URLField(verbose_name='ссылка на видео', **NULLABLE, help_text='Вставте ссылку на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE, help_text='Укажите курс')
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name='Стоимость урока', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE, help_text='Укажите курс')

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
