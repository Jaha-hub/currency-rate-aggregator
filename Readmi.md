Currency Rate Aggregator

Currency Rate Aggregator — это сервис для получения, хранения и анализа валютных курсов.
Проект собирает курсы валют из внешнего API, сохраняет их и позволяет работать с ними через backend-логику.

🚀 Возможности

Получение актуальных курсов валют через API

Конвертация валют

Хранение курсов в базе данных

Анализ балансов пользователя

Поддержка нескольких валют

Асинхронная работа (async Python)

Работа через Docker

🛠 Технологии

Проект использует:

Python 3.11+

FastAPI

SQLAlchemy (Async)

PostgreSQL

Docker

Poetry

HTTPX

📦 Установка

1. Клонировать репозиторий
   git clone https://github.com/your-username/currency-rate-aggregator.git
   cd currency-rate-aggregator
2. Установить зависимости

Через Poetry:

poetry install

Активировать окружение:

poetry shell
🐳 Запуск через Docker
docker-compose up -d --build

После запуска сервис будет доступен:

http://localhost:8000
⚙️ Переменные окружения

Пример .env:

DB_HOST=postgres
DB_PORT=5432
DB_NAME=currency
DB_USER=postgres
DB_PASSWORD=postgres

API_KEY=your_api_key
💱 Источник курсов валют

Проект использует API:

https://api.exchangerate.host

Пример запроса:

GET /live?currencies=USD,EUR,RUB,UZS
📊 Пример данных
{
"USD": 1,
"EUR": 0.91,
"RUB": 89.12,
"UZS": 12650
}
🧪 Тестирование

Запуск тестов:

pytest
📌 Roadmap

Планируемые улучшения:

кеширование курсов

поддержка нескольких API

графики изменения валют

WebSocket обновления курсов

👤 Автор

Sanjar