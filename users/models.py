from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Введите электронную почту')
    phone_number = models.CharField(max_length=15, verbose_name='Phone', blank=True, null=True, help_text='Введите номер телефона')
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Avatar', blank=True, null=True)
    country = models.CharField(max_length=50, verbose_name='Country', blank=True, null=True, help_text='Введите страну')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

