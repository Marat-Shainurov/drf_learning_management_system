# Инструкция по запуску приложения 

1. Установить docker, выбрав соответствующую ОС.
   https://docs.docker.com/get-docker/

2. Клонировать в IDE проект https://github.com/Marat-Shainurov/drf_lms_cw.git на вашу локальную машину.

3. Запустить процесс создания и запусука образа приложения, с помощью команд:
   - docker-compose build
   - docker-compose up

4. Применить миграции базы данных, с помощью команды:
   - docker-compose exec app python manage.py migrate

5. Изучить документацию проекта (swagger или redoc):
   - http://127.0.0.1:8000/swagger/
   - http://127.0.0.1:8000/redoc/

6. Открыть в браузере главную страницу проекта http://127.0.0.1:8000/ , и начать работу с эндпоинтами.
7. 
   

