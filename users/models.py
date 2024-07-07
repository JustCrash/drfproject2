from django.db import models
from django.contrib.auth.models import AbstractUser
from lms.models import Course, Lesson


NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):
    name = None
    username = None
    email = models.EmailField(unique=True, verbose_name='почта', help_text='Введите почту')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE, help_text='Введите номер телефона')
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='аватар', **NULLABLE, help_text='Вставъте аватарку')
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE, help_text='Введите город')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', help_text='Укажите пользователя', **NULLABLE)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты', help_text='Укажите дату оплаты')
    payment_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    payment_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    choices_method = {'Наличными': 'Наличными', 'Без наличный': 'Без наличный'}
    payment_method = models.CharField(max_length=20, default='card', verbose_name='Способ оплаты', choices=choices_method)
    session_id = models.CharField(max_length=255, verbose_name='ID сессии', **NULLABLE)
    payment_link = models.URLField(max_length=400, verbose_name='Ссылка на оплату', **NULLABLE)

    def __str__(self):
        return f'{self.user}: {self.payment_lesson if self.payment_lesson else self.payment_course}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
