# Используем легковесный официальный образ Python
FROM python:3.10-slim

# Устанавливаем системные зависимости для компиляции драйвера БД
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY app.py .

# Декларируем порт (внутренний)
EXPOSE 5000

# Запуск приложения
CMD ["python", "app.py"]