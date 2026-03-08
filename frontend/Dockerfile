# Используем стабильный Node LTS
FROM node:20-alpine

# Рабочая директория
WORKDIR /app

# Копируем зависимости
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем весь код
COPY . .

# Собираем production-версию
RUN npm run build

# Устанавливаем простой сервер для раздачи статики
RUN npm install -g serve

EXPOSE 3000

# Запуск production build
CMD ["serve", "-s", "build", "-l", "3000"]