from users.models import User


def start(update, context):
    telegram_id = update.message.chat_id
    email = update.message.text

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        update.message.reply_text(
            "Пользователь с таким email не найден. Проверьте правильность ввода!"
        )
        return

    profile, created = User.objects.get_or_create(user=user)
    profile.telegram_id = telegram_id
    profile.save()
    context.bot.send_message(chat_id=telegram_id, text="Telegram успешно привязан!")
