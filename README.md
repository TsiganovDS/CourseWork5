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
### 1. Клонируй репозиторий:
#### git clone https://github.com/TsiganovDS/CourseWork5
#### cd CourseWork5
### 2. Создай .env на основе шаблона:
#### SECRET_KEY=укажи_свой_секретный_ключ
#### DEBUG=True
#### ALLOWED_HOSTS=127.0.0.1,localhost

#### NAME=postgres
#### USER=postgres
#### PASSWORD=postgres
#### HOST=
#### PORT=5432

#### CELERY_BROKER_URL=redis://redis:6379/0
### 3. Собери и запусти проект:
#### docker compose up --build
### 4. Открой в браузере:
#### http://localhost

## CI/CD
### Настроен GitHub Actions workflow .github/workflows/deploy.yml
#### Автоматически запускается:
#### при push в ветку develop
#### выполняет тесты и линтинг
#### при успехе — деплой на сервер через SSH
