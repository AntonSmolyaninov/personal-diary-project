# 📔 Личный дневник на Django

## 📝 Описание проекта

Веб-приложение для ведения личного дневника. Позволяет пользователям создавать, редактировать, удалять и искать свои записи.

### Основной функционал

- ✅ Регистрация и аутентификация пользователей
- ✅ Расширенный профиль пользователя (аватар, биография, телефон, дата рождения)
- ✅ Создание, чтение, обновление, удаление записей (CRUD)
- ✅ Поиск по заголовку и содержанию
- ✅ Пагинация (10 записей на странице)
- ✅ Права доступа (пользователь видит и редактирует только свои записи)
- ✅ Адаптивный дизайн на Bootstrap 5 с фоновым изображением
- ✅ Админ-панель Django
- ✅ Контейнеризация Docker и Docker Compose

## 🛠 Технологии

| Компонент | Технология |
|-----------|------------|
| Backend | Python 3.12, Django 6.0 |
| Database | PostgreSQL 15 |
| Frontend | Bootstrap 5, Django Templates |
| Containerization | Docker, Docker Compose |
| Server | Gunicorn |
| Дополнительно | Pillow (для аватаров), python-dotenv |

## 📁 Структура проекта
personal-diary-project/
├── config/ # Настройки Django
│ ├── settings.py # Конфигурация проекта
│ ├── urls.py # Главные маршруты
│ └── wsgi.py
├── users/ # Приложение для аутентификации
│ ├── models.py # Profile (расширение User)
│ ├── views.py # LoginView, RegisterView, ProfileView
│ ├── forms.py # Формы регистрации и редактирования
│ ├── urls.py # Маршруты /users/*
│ └── templates/users/ # Шаблоны пользователей
├── diary/ # Приложение для записей
│ ├── models.py # Entry (запись дневника)
│ ├── views.py # CRUD представления
│ ├── forms.py # EntryForm
│ ├── urls.py # Маршруты записей
│ ├── admin.py # Регистрация в админке
│ └── templates/diary/ # Шаблоны записей
├── templates/
│ └── base.html # Базовый шаблон с Bootstrap
├── static/
│ └── images/ # Фоновые изображения
├── media/ # Загруженные файлы (аватары)
├── staticfiles/ # Собранная статика
├── .env # Переменные окружения
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

## 🚀 Быстрый старт

### Требования

- Docker Desktop (для Windows/Mac) или Docker (для Linux)
- Git (опционально)

### Запуск через Docker (рекомендуется)

```bash
# 1. Клонирование репозитория
git clone https://github.com/ВАШ_ЛОГИН/personal-diary-project.git
cd personal-diary-project

# 2. Создайте файл .env (или используйте пример ниже)
# cat > .env << EOF
# SECRET_KEY=django-insecure-your-secret-key
# DEBUG=True
# NAME=diary_db
# USER=postgres
# PASSWORD=your_password
# HOST=db
# PORT=5432
# EOF

# 3. Запустите контейнеры
docker-compose up -d --build

# 4. Выполните миграции
docker-compose exec web python manage.py migrate

# 5. Создайте суперпользователя
docker-compose exec web python manage.py createsuperuser

# 6. Откройте в браузере
# http://localhost:8000
Локальный запуск (без Docker)
bash
# 1. Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate

# 2. Установите зависимости
pip install -r requirements.txt

# 3. Настройте PostgreSQL и создайте базу данных
# Создайте файл .env с параметрами подключения

# 4. Выполните миграции
python manage.py migrate

# 5. Создайте суперпользователя
python manage.py createsuperuser

# 6. Запустите сервер
python manage.py runserver
🐳 Docker команды
bash
# Запуск в фоновом режиме
docker-compose up -d

# Запуск с логами
docker-compose up

# Остановка
docker-compose down

# Остановка с удалением томов (очистка БД)
docker-compose down -v

# Просмотр логов
docker-compose logs -f

# Просмотр логов конкретного сервиса
docker-compose logs -f web

# Выполнить команду в контейнере
docker-compose exec web python manage.py migrate

# Войти в контейнер web
docker-compose exec web bash

# Войти в контейнер БД
docker-compose exec db psql -U postgres -d diary_db

# Пересобрать образы
docker-compose up --build

# Проверить статус контейнеров
docker-compose ps

📱 Страницы и URL
URL	Описание
/	Главная страница (список записей)
/users/login/	Вход в систему
/users/logout/	Выход из системы
/users/register/	Регистрация
/users/profile/	Просмотр профиля
/users/profile/edit/	Редактирование профиля
/entry/create/	Создание записи
/entry/<id>/	Просмотр записи
/entry/<id>/update/	Редактирование записи
/entry/<id>/delete/	Удаление записи
/admin/	Админ-панель Django
📝 Пример использования
Регистрация: перейдите на /users/register/, создайте аккаунт

Создание записи: нажмите "Новая запись", введите заголовок и текст

Поиск: используйте строку поиска на главной странице

Редактирование: нажмите "Редактировать" на любой записи

Удаление: нажмите "Удалить" и подтвердите действие

Профиль: загрузите аватар, укажите телефон и дату рождения

👨‍💻 Автор
Anton Smolyaninov
