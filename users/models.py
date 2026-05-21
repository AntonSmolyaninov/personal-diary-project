from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Профиль пользователя (расширение стандартной модели User)."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='profile'
    )

    bio = models.TextField(
        verbose_name='О себе',
        max_length=500,
        blank=True,
        help_text='Расскажите немного о себе'
    )

    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='avatars/',
        blank=True,
        null=True
    )

    phone = models.CharField(
        verbose_name='Телефон',
        max_length=20,
        blank=True
    )

    birth_date = models.DateField(
        verbose_name='Дата рождения',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        verbose_name='Дата создания профиля',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Автоматически создаёт профиль при создании пользователя."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Автоматически сохраняет профиль при сохранении пользователя."""
    instance.profile.save()
