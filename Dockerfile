# Используем минимальный официальный Python-образ
FROM python:3.11-slim

# Создаём папку приложения
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код бота
COPY . .

# Указываем стандартную команду на запуск
CMD ["python", "bot/main.py"]
