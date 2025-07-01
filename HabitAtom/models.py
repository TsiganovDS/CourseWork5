from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    is_pleasant = models.BooleanField(default=False, helptext="Приятная привычка?")
    related_habit = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='linked_habits',
        help_text="Связанная полезная привычка"
    )
    period = models.PositiveSmallIntegerField(default=1, help_text="Периодичность в днях")
    reward = models.CharField(max_length=255, blank=True)
    duration = models.PositiveSmallIntegerField(help_text="Время на выполнение в минутах")
    is_public = models.BooleanField(default=False, help_text="Публичная привычка?")

    def __str__(self):
        return f'{self.action} в {self.place} в {self.time}'