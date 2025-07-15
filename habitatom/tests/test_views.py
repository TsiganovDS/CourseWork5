from django.test import Client, TestCase
from django.urls import reverse

from habitatom.models import Habit
from users.models import User


class HabitTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email="test@email.com", password="password123"
        )
        self.client.login(email="test@email.com", password="password123")
        self.habit = Habit.objects.create(
            name="Exercise daily", user=self.user, duration=3
        )

    def test_habit_list_view(self):
        response = self.client.get(reverse("habit_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "habitatom/habit_list.html")
        habits_in_context = response.context["habits"]
        self.assertIn(self.habit, habits_in_context)

    def test_habit_detail_view(self):
        response = self.client.get(reverse("habit_detail", args=(self.habit.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "habitatom/habit_detail.html")
        habit_in_context = response.context["habit"]
        self.assertEqual(habit_in_context, self.habit)

    def test_habit_delete_view(self):
        response = self.client.post(
            reverse("habit_confirm_delete", args=(self.habit.id,))
        )
        self.assertRedirects(response, reverse("habit_list"))
        with self.assertRaises(Habit.DoesNotExist):
            Habit.objects.get(id=self.habit.id)
