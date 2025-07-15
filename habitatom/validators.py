from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_habit_fields(habit):
    if habit.reward and habit.related_habit:
        raise ValidationError(
            "Можно заполнить только одно из полей: вознаграждение или связанная привычка."
        )


def validate_pleasant_habit(habit):
    if habit.is_pleasant and (habit.reward or habit.related_habit):
        raise ValidationError(
            "У приятной привычки не может быть вознаграждения или связанной привычки."
        )


def validate_performance(habit):
    if habit.last_performed:
        days_since_last_performance = (
            timezone.now().date() - habit.last_performed
        ).days
        if days_since_last_performance > 7:
            raise ValidationError("Нельзя не выполнять привычку более 7 дней.")
