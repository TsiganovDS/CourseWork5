import unittest
from unittest.mock import MagicMock, patch

from django.utils import timezone

from habitatom.tasks import check_and_send_habit_reminders


class CheckAndSendHabitRemindersTest(unittest.TestCase):

    @patch("habitatom.tasks.requests.get")
    @patch("habitatom.models.Habit")
    @patch("habitatom.tasks.get_user_model")
    @patch("django.utils.timezone.localtime")
    def test_no_telegram_id(
        self, mock_localtime, mock_get_user_model, mockHabit, mock_requests_get
    ):
        now = timezone.now().replace(hour=7, minute=30)
        mock_localtime.return_value = now

        mock_habit = MagicMock()
        mock_habit.user.id = 1
        mock_habit.action = "попить воду"
        mock_habit.place = "кухне"
        mockHabit.objects.filter.return_value = [mock_habit]

        mock_user = MagicMock()
        mock_user.telegram_id = None
        mock_get_user_model.return_value.objects.get.return_value = mock_user

        check_and_send_habit_reminders()

        mock_requests_get.assert_not_called()

    @patch("habitatom.tasks.requests.get")
    @patch("habitatom.models.Habit")
    @patch("habitatom.tasks.get_user_model")
    @patch("django.utils.timezone.localtime")
    def test_user_does_not_exist(
        self, mock_localtime, mock_get_user_model, mockHabit, mock_requests_get
    ):
        now = timezone.now().replace(hour=7, minute=30)
        mock_localtime.return_value = now

        mock_habit = MagicMock()
        mock_habit.user.id = 1
        mock_habit.action = "попить воду"
        mock_habit.place = "кухне"
        mockHabit.objects.filter.return_value = [mock_habit]

        mock_get_user_model.return_value.objects.get.side_effect = Exception(
            "User.DoesNotExist"
        )

        check_and_send_habit_reminders()
        mock_requests_get.assert_not_called()


if __name__ == "__main__":
    unittest.main()
