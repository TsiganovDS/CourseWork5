# Указываем базовый образ
FROM python:3.10

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app


RUN apt-get update && \\
    apt-get install -y build-essential libpq-dev && \\
    rm -rf /var/lib/apt/lists/*

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt ./
RUN pip install -r requirements.txt


# Открываем порт 8000 для взаимодействия с приложением
EXPOSE 8000

COPY . .

# Определяем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]