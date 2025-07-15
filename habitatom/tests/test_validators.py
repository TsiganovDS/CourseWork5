import unittest

from django.core.exceptions import ValidationError
from django.utils import timezone

from habitatom.validators import (validate_habit_fields, validate_performance,
                                  validate_pleasant_habit)


class Habit:
    def __init__(
        self, reward=None, related_habit=None, is_pleasant=False, last_performed=None
    ):
        self.reward = reward
        self.related_habit = related_habit
        self.is_pleasant = is_pleasant
        self.last_performed = last_performed


class TestHabitValidators(unittest.TestCase):

    def test_validate_habit_fields_only_reward(self):
        habit = Habit(reward="Пицца", related_habit=None)
        validate_habit_fields(habit)

    def test_validate_habit_fields_only_related(self):
        habit = Habit(reward=None, related_habit=object())
        validate_habit_fields(habit)

    def test_validate_habit_fields_both_filled(self):
        habit = Habit(reward="Кофе", related_habit=object())
        with self.assertRaises(ValidationError):
            validate_habit_fields(habit)

    def test_validate_pleasant_habit_ok(self):
        habit = Habit(is_pleasant=True, reward=None, related_habit=None)
        validate_pleasant_habit(habit)

    def test_validate_pleasant_habit_with_reward(self):
        habit = Habit(is_pleasant=True, reward="Шоколадка", related_habit=None)
        with self.assertRaises(ValidationError):
            validate_pleasant_habit(habit)

    def test_validate_pleasant_habit_with_related(self):
        habit = Habit(is_pleasant=True, reward=None, related_habit=object())
        with self.assertRaises(ValidationError):
            validate_pleasant_habit(habit)

    def test_validate_performance_none(self):
        habit = Habit(last_performed=None)
        validate_performance(habit)

    def test_validate_performance_recent(self):
        habit = Habit(last_performed=timezone.now().date())
        validate_performance(habit)

    def test_validate_performance_old(self):
        habit = Habit(last_performed=timezone.now().date() - timezone.timedelta(days=8))
        with self.assertRaises(ValidationError):
            validate_performance(habit)


if __name__ == "main":
    unittest.main()
