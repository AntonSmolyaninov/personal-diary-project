from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    """Форма регистрации нового пользователя с Bootstrap стилями."""

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))

    bio = forms.CharField(
        label="О себе",
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
    )

    phone = forms.CharField(
        label="Телефон", max_length=20, required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    birth_date = forms.DateField(
        label="Дата рождения", required=False, widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )

    avatar = forms.ImageField(label="Аватар", required=False, widget=forms.FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if hasattr(field.widget, "attrs"):
                field.widget.attrs.update({"class": "form-control"})

    def save(self, commit=True):
        """Сохраняет пользователя и профиль."""
        user = super().save(commit=True)

        profile = user.profile
        profile.bio = self.cleaned_data.get("bio", "")
        profile.phone = self.cleaned_data.get("phone", "")
        profile.birth_date = self.cleaned_data.get("birth_date", None)

        if self.cleaned_data.get("avatar"):
            profile.avatar = self.cleaned_data.get("avatar")

        profile.save()

        return user


class UserUpdateForm(forms.ModelForm):
    """Форма для редактирования основных данных пользователя."""

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class ProfileUpdateForm(forms.ModelForm):
    """Форма для редактирования профиля."""

    class Meta:
        model = Profile
        fields = ["bio", "phone", "birth_date", "avatar"]
        widgets = {
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "birth_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "avatar": forms.FileInput(attrs={"class": "form-control"}),
        }
