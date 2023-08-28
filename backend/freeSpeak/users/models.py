from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    first_name = models.CharField(
        verbose_name="Имя",
        max_length=100,
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=100,
    )
    username = models.CharField(
        max_length=100,
        unique=True,
        validators=[UnicodeUsernameValidator()],
    )
    email = models.EmailField(
        verbose_name="Email",
        unique=True,
        max_length=255,
    )
    profile = models.ForeignKey(
        'Profile',
        related_name='profile',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)


class Profile(models.Model):
    user = models.ForeignKey(
        User,
        related_name='owner',
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='avatars'
    )
    status = models.CharField(
        verbose_name='Статус пользователя',
        max_length=100
    )

    def __str__(self):
        return self.user.__str__()
