from django.contrib import admin

from diary.models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    """Отображение записей в админ-панели Django."""

    list_display = ['title', 'author', 'created_at', 'updated_at']
    list_filter = ['author', 'created_at']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'
