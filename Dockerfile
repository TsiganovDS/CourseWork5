# Используем минималистичный образ Python
FROM python:3.11-slim-bullseye as base

# Настраиваем рабочую директорию
WORKDIR /code

# Клонируем исходники проекта
COPY . /code

# Устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# По умолчанию запускаем простейшую команду
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]