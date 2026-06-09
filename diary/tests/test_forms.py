"""
Тесты для форм приложения diary.
"""

import pytest

from diary.forms import EntryForm


@pytest.mark.django_db
class TestEntryForm:
    """Тесты для формы EntryForm."""

    def test_valid_form(self):
        """Тест валидной формы."""
        form = EntryForm(data={"title": "Заголовок записи", "content": "Содержание записи"})
        assert form.is_valid()

    def test_empty_title(self):
        """Тест: заголовок обязателен."""
        form = EntryForm(data={"title": "", "content": "Содержание"})
        assert not form.is_valid()
        assert "title" in form.errors

    def test_empty_content(self):
        """Тест: содержание обязательно."""
        form = EntryForm(data={"title": "Заголовок", "content": ""})
        assert not form.is_valid()
        assert "content" in form.errors

    def test_max_title_length(self):
        """Тест: максимальная длина заголовка."""
        long_title = "A" * 201
        form = EntryForm(data={"title": long_title, "content": "Содержание"})
        assert not form.is_valid()
        assert "title" in form.errors
