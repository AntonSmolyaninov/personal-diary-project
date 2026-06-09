from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Entry(models.Model):
    """Модель записи дневника"""

    title = models.CharField(verbose_name="Заголовок", max_length=50, help_text="Краткий заголовок Вашей записи")

    content = models.TextField(verbose_name="Содержание", help_text="Текст Вашей записи")

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now=True,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name="entries",
        help_text="Пользователь, создавший запись",
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("entry_detail", args=[self.pk])
