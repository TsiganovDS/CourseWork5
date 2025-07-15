import requests
from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

from habitatom.models import Habit

User = get_user_model()


@shared_task
def check_and_send_habit_reminders():
    now = timezone.localtime()
    current_hour = now.hour
    current_minute = now.minute
    habits = Habit.objects.filter(time__hour=current_hour, time__minute=current_minute)
    for habit in habits:
        try:
            user = User.objects.get(id=habit.user.id)
            chat_id = getattr(user, "telegram_id", None)
            if chat_id:
                message = f"Напоминание! Вам нужно {habit.action} в {habit.place}."
                url = f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage"
                params = {"chat_id": chat_id, "text": message}
                requests.get(url, params=params)
        except User.DoesNotExist:
            continue
