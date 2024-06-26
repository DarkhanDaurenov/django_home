from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE_FIELDS


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', **NULLABLE_FIELDS, help_text='Загрузите фото')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE_FIELDS, help_text='Введите номер телефона')
    country = models.CharField(max_length=150, verbose_name='Страна', help_text='Введите страну')

    token = models.CharField(max_length=100, verbose_name='Токен', **NULLABLE_FIELDS)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email