# Трекер полезных привычек
### Проект Django REST Framework для отслеживания и управления полезными привычками с напоминаниями. Реализована интеграция с Telegram, Celery для фоновых задач, Redis как брокер, PostgreSQL как БД, и автоматический деплой на сервер через GitHub Actions.
## Возможности
### Регистрация и авторизация пользователей
### Создание личных и публичных привычек
### Уведомления через Telegram
### Автоматические напоминания с Celery и Beat
### Права доступа: только владелец может редактировать привычки
### Документация OpenAPI/Swagger
### CI/CD с тестами и автодеплоем
## Стек технологий
### Python 3.10
### Django 4+
### Django REST Framework
### PostgreSQL
### Redis
### Celery + Celery Beat
### Docker, Docker Compose
### GitHub Actions (CI/CD)
### Yandex Cloud (деплой)
##  Установка и запуск проекта локально (Docker)
### 1. Клонируйте репозиторий:
#### git clone https://github.com/TsiganovDS/CourseWork5
#### cd CourseWork5
### 2. Создайте .env на основе шаблона:
#### SECRET_KEY=укажите_свой_секретный_ключ
#### DEBUG=True
#### ALLOWED_HOSTS=127.0.0.1,localhost
#### NAME=
#### USER=
#### PASSWORD=
#### HOST=
#### PORT=5432
#### CELERY_BROKER_URL=redis://redis:6379/0
### 3. Соберите и запустите проект:
#### docker compose up --build
### 4. Откройте в браузере:
#### http://127.0.0.1:8000

## CI/CD
### Настроен GitHub Actions workflow .github/workflows/main.yml
### Перед началом установки убедитесь, что ваш сервер соответствует следующим требованиям:

#### - Операционная система: Linux (Ubuntu, Debian и т.п.)
#### - Установлен Docker Engine >= v20.xx (установите последнюю версию)
#### - Установлен Docker Compose >= v2.xx (желательно последней версии)
#### - Открытые порты:
####  - TCP порт 22 (для SSH-доступа)
####  - TCP порт 80 (HTTP трафик)
####  - TCP порт 443 (HTTPS трафик)

## 1. Подключение к серверу через SSH
### ssh -l test 158.160.146.211
## 2. Копирование файлов на сервер
### Скопируйте архив проекта на сервер или создайте репозиторий и загрузите проект через Git:
### git clone https://github.com/TsiganovDS/CourseWork5
### cd CourseWork5
## 3.  Подготовка переменной окружения (.env)
### Создайте файл .env на сервере и заполните его необходимыми параметрами:
#### SECRET_KEY=your_secret_key_here
#### DEBUG=False
#### ALLOWED_HOSTS=your_domain_or_IP
#### DB_ENGINE=django.db.backends.postgresql
#### NAME=database_name
#### USER=database_user
#### PASSWORD=database_password
#### HOST=db_host
#### PORT=5432
#### REDIS_URL=redis://redis:6379/0
#### CELERY_BROKER_URL=redis://redis:6379/0
#### TELEGRAM_TOKEN=telegram_bot_token
## 4.  Первый запуск
### Перед первым запуском выполните инициализацию базы данных и миграцию моделей:
#### docker compose up -d --build
###  Затем проверьте состояние контейнеров:
#### docker ps
## 5. Обновление проекта
###  После внесения изменений выполните обновление Docker-образов и перезагрузите контейнеры:
#### docker compose pull
#### docker compose up -d --remove-orphans




