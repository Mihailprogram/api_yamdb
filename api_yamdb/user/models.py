from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_ROLE_USER = 'user'
    USER_ROLE_MODERATOR = 'moderator'
    USER_ROLE_ADMIN = 'admin'

    USER_ROLE_CHOICES = (
        (USER_ROLE_USER, 'Пользователь'),
        (USER_ROLE_MODERATOR, 'Модератор'),
        (USER_ROLE_ADMIN, 'Админ')
    )

    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Электронная почта'
    )
    role = models.CharField(
        max_length=16,
        choices=USER_ROLE_CHOICES,
        default=USER_ROLE_USER,
        verbose_name='Роль'
    )
    bio = models.TextField(blank=True,verbose_name='Описание')
    confirmation_code = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Код для авторизации'
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email'
            )
        ]

    @property
    def is_user(self):
        if self.role == self.USER_ROLE_USER:
            return True
        else:
            return False

    @property
    def is_moderator(self):
        if self.role == self.USER_ROLE_MODERATOR:
            return True
        else:
            return False

    @property
    def is_admin(self):
        if self.role == self.USER_ROLE_ADMIN:
            return True
        else:
            return False


User = get_user_model()
