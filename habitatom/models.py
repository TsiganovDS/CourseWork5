from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from config.settings import AUTH_USER_MODEL

from .validators import (validate_habit_fields, validate_performance,
                         validate_pleasant_habit)

User = get_user_model()


class Habit(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="habits",
        verbose_name="Пользователь",
    )
    place = models.CharField(
        max_length=255,
        verbose_name="Место для выполнения привычки",
        help_text="Напиши место",
    )
    time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Время",
        help_text="Время для выполнения привычки",
    )
    action = models.CharField(
        max_length=255,
        verbose_name="Действие",
        help_text="Напиши что делаешь",
    )
    is_pleasant = models.BooleanField(default=False, help_text="Приятная привычка?")
    last_performed = models.DateTimeField(
        blank=True, null=True, help_text="Дата и время последнего выполнения"
    )
    related_habit = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="linked_habits",
        help_text="Связанная полезная привычка",
    )
    period = models.PositiveSmallIntegerField(
        default=1, help_text="Периодичность в днях"
    )
    reward = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Вознаграждение",
        help_text="чем пользователь должен себя вознаградить после выполнения",
    )
    duration = models.PositiveSmallIntegerField(
        help_text="Время на выполнение в минутах"
    )
    is_public = models.BooleanField(default=False, help_text="Публичная привычка?")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def clean(self):
        validate_habit_fields(self)
        validate_pleasant_habit(self)
        validate_performance(self)

    def save(self, *args, **kwargs):
        if self.pk is not None and self.last_performed:
            time_taken = (timezone.now() - self.last_performed).total_seconds()
            if time_taken > 120:
                raise ValidationError(
                    "Время выполнения не должно превышать 120 секунд."
                )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.action} в {self.place} в {self.time}"
