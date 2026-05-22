from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile


class ProfileInline(admin.StackedInline):
    """Встраиваем профиль в страницу редактирования пользователя."""

    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    """Расширенная админка для пользователей."""

    inlines = [ProfileInline]
    list_display = ["username", "email", "first_name", "last_name", "is_staff"]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone", "created_at"]
    search_fields = ["user__username", "phone"]
