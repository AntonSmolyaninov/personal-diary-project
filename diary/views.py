from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Entry
from .forms import EntryForm


class EntryListView(LoginRequiredMixin, ListView):
    """
    Список записей пользователя.
    Поддерживает поиск по заголовку и содержанию.
    """

    model = Entry
    template_name = 'diary/entry_list.html'
    context_object_name = 'entries'
    paginate_by = 10

    def get_queryset(self):
        queryset = Entry.objects.filter(author=self.request.user)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class EntryDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Детальный просмотр записи."""

    model = Entry
    template_name = 'diary/entry_detail.html'

    def test_func(self):
        return self.request.user == self.get_object().author


class EntryCreateView(LoginRequiredMixin, CreateView):
    """Создание новой записи."""

    model = Entry
    form_class = EntryForm
    template_name = 'diary/entry_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Редактирование записи."""

    model = Entry
    form_class = EntryForm
    template_name = 'diary/entry_form.html'

    def test_func(self):
        return self.request.user == self.get_object().author


class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Удаление записи."""

    model = Entry
    template_name = 'diary/entry_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().author
