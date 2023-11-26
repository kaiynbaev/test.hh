# test.hh
celery+redis+django+docker
celery+redis+django+docker ... клонируете репозиторий на свой хост ... создаете файл .env, создаете внутри переменную EMAIL_HOST_PASSWORD = '16 значный пароль приложения от gmail (smtp настроен именно на gmail)' ... docker compose up -d --build --remove-orphans # start ... порты которые используются в docker compose должны быть свободны ... Далее суперпользователя, заходим внутрь контейнера докер " docker exec -it <container_id> /bin/sh " ... python3 manage.py createsuperuser ... далее заходите в админку (/admin) ... ПОСТ запрос доступен по адресу /api/registration/ ...
Примечание: метод пост api/registration принимает параметры username, email, password, password2.
