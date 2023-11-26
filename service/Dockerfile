# Используем официальный образ Python 3.10
FROM python:3.10

# Устанавливаем рабочую директорию в /app
WORKDIR /service 

# Копируем зависимости проекта (если они есть)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip3 install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в текущую директорию образа
COPY . .

# Команда для запуска вашего приложения
CMD ["python3", "manage.py", "migrate"]

