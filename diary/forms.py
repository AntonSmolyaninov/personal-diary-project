from django import forms

from .models import Entry


class EntryForm(forms.ModelForm):
    """Форма для создания и редактирования записи дневника."""

    class Meta:
        model = Entry
        fields = ["title", "content"]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Например: Мои мысли на сегодня..."}
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 10,
                    "placeholder": "Напишите здесь всё, что хотите запомнить...",
                }
            ),
        }
