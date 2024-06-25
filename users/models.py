from django.db import models
from django.contrib.auth.models import AbstractUser


NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):
    name = None
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
