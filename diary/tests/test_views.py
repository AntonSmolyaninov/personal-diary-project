import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from diary.models import Entry


@pytest.mark.django_db
class TestEntryListView:
    """Тесты для списка записей."""

    def test_login_required(self, client):
        """Тест: доступ только для авторизованных."""
        response = client.get(reverse("entry_list"))
        assert response.status_code == 302
        assert "/users/login/" in response.url

    def test_authenticated_access(self, client):
        """Тест: авторизованный пользователь видит страницу."""
        user = User.objects.create_user(username="testuser")
        client.force_login(user)

        response = client.get(reverse("entry_list"))
        assert response.status_code == 200
        assert "Мои записи" in response.content.decode()
        assert "Новая запись" in response.content.decode()

    def test_only_own_entries(self, client):
        """Тест: пользователь видит только свои записи."""
        user1 = User.objects.create_user(username="user1")
        user2 = User.objects.create_user(username="user2")

        Entry.objects.create(title="Запись user1", content="Содержание", author=user1)
        Entry.objects.create(title="Запись user2", content="Содержание", author=user2)

        client.force_login(user1)
        response = client.get(reverse("entry_list"))
        content = response.content.decode()

        assert "Запись user1" in content
        assert "Запись user2" not in content
