"""
Тесты для моделей приложения diary.
"""

import time

import pytest
from django.contrib.auth.models import User
from django.db import IntegrityError

from diary.models import Entry


@pytest.mark.django_db
class TestEntryModel:
    """Тесты для модели Entry."""

    def test_create_entry(self):
        """Тест создания записи."""
        user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass123")

        entry = Entry.objects.create(title="Тестовая запись", content="Это содержание тестовой записи", author=user)

        assert entry.title == "Тестовая запись"
        assert entry.content == "Это содержание тестовой записи"
        assert entry.author == user
        assert entry.pk is not None

    def test_entry_str_method(self):
        """Тест строкового представления записи."""
        user = User.objects.create_user(username="testuser")
        entry = Entry.objects.create(title="Моя запись", content="Содержание", author=user)

        assert str(entry) == "Моя запись"

    def test_entry_ordering(self):
        """Тест сортировки записей (новые сверху)."""
        user = User.objects.create_user(username="testuser")

        entry1 = Entry.objects.create(title="Старая запись", content="Содержание 1", author=user)

        time.sleep(0.1)

        entry2 = Entry.objects.create(title="Новая запись", content="Содержание 2", author=user)

        entries = Entry.objects.all()
        assert entries[0] == entry2  # Первая — новая
        assert entries[1] == entry1  # Вторая — старая

    def test_entry_absolute_url(self):
        """Тест метода get_absolute_url."""
        user = User.objects.create_user(username="testuser")
        entry = Entry.objects.create(title="Запись", content="Содержание", author=user)

        assert entry.get_absolute_url() == f"/entry/{entry.pk}/"

    def test_entry_author_required(self):
        """Тест: запись должна иметь автора."""
        with pytest.raises(IntegrityError):
            Entry.objects.create(title="Запись без автора", content="Содержание")

    def test_entry_verbose_names(self):
        """Тест verbose_name модели."""
        assert Entry._meta.verbose_name == "Запись"
        assert Entry._meta.verbose_name_plural == "Записи"
