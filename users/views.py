from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import CustomUserCreationForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile


class CustomLoginView(LoginView):
    """Страница входа в систему."""

    template_name = "users/login.html"


class RegisterView(CreateView):
    """Страница регистрации нового пользователя."""

    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")


class ProfileView(LoginRequiredMixin, DetailView):
    """Просмотр профиля пользователя."""

    model = Profile
    template_name = "users/profile.html"
    context_object_name = "profile"

    def get_object(self):
        return self.request.user.profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование профиля пользователя."""

    model = Profile
    form_class = ProfileUpdateForm
    template_name = "users/profile_edit.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["user_form"] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context["user_form"] = UserUpdateForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = self.get_form()

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Профиль успешно обновлён!")
            return redirect(self.get_success_url())

        return self.render_to_response(self.get_context_data(user_form=user_form, form=profile_form))
