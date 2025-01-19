FROM nginx:latest

# создаем директорию для статических файлов
RUN mkdir -p /app/staticfiles

# копируем кофигурацию nginx в контейнер
COPY nginx.conf /etc/nginx/nginx.conf

# открываем порт 80  для HTTP трафика
EXPOSE 80
