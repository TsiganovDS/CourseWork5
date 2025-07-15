from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from rest_framework import viewsets

from .models import Habit, get_user_model
from .serializers import HabitSerializer

User = get_user_model()


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitListView(LoginRequiredMixin, ListView):
    model = Habit
    template_name = "habitatom/habit_list.html"
    context_object_name = "habits"
    paginate_by = 5

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user).order_by("-name")


class HabitDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Habit
    template_name = "habitatom/habit_detail.html"
    context_object_name = "habit"

    def test_func(self):
        habit = self.get_object()
        return habit.user == self.request.user


class HabitCreateView(LoginRequiredMixin, CreateView):
    model = Habit
    template_name = "habitatom/habit_form.html"
    fields = "__all__"
    success_url = reverse_lazy("habit_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class HabitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Habit
    template_name = "habitatom/habit_form.html"
    fields = ["name", "time", "action"]
    success_url = reverse_lazy("habit_list")

    def test_func(self):
        habit = self.get_object()
        return habit.user == self.request.user


class HabitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Habit
    template_name = "habitatom/habit_confirm_delete.html"
    success_url = reverse_lazy("habit_list")

    def test_func(self):
        habit = self.get_object()
        return habit.user == self.request.user
