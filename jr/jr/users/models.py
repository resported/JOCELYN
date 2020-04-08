from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse


class User(User):

    def __str__(self):
        return ''.format(self.username)

    def get_user(self):
        return reverse('current_user', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
