from django.db import models
from django.contrib.auth import get_user_model
from .validators import validate_habit_fields, validate_pleasant_habit, validate_performance
from django.core.exceptions import ValidationError
from django.utils import timezone

User = get_user_model()

class Habit(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    is_pleasant = models.BooleanField(default=False, help_text="Приятная привычка?")
    last_performed = models.DateField(blank=True, null=True, help_text="Дата последнего выполнения")
    related_habit = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='linked_habits',
        help_text="Связанная полезная привычка"
    )
    period = models.PositiveSmallIntegerField(default=1, help_text="Периодичность в днях")
    reward = models.CharField(max_length=255, blank=True)
    duration = models.PositiveSmallIntegerField(help_text="Время на выполнение в минутах")
    is_public = models.BooleanField(default=False, help_text="Публичная привычка?")

    def clean(self):
        validate_habit_fields(self)
        validate_pleasant_habit(self)
        validate_performance(self)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            if self.last_performed:
                time_taken = (timezone.now() - self.last_performed).total_seconds() / 60
                if time_taken > 120:
                    raise ValidationError("Время выполнения не должно превышать 120 секунд.")

        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.action} в {self.place} в {self.time}'