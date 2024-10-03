## Запуск приложения

> Загрузка проекта
```bash
https://github.com/Aroptich/Cat_show.git
cd Cat_show
```
## Установка зависимостей

> Установка библиотеки __poetry__
```bash
pip install poetry
```
> Установка всех зависимостей приложения
```bash
poetry install
```
> Активирование вертуальной среды
```bash
poetry shell
```
> Установка миграций

```bash
python manage.py makemigrations
python manage.py migrate
```

> Предварительная загрузка информации в базу данных
```bash
python manage.py loaddata ????.json
```

> Запуск сервера
```bash
python manage.py runserver
```
Открыть приложение в браузере по адресу [localhost:8000](http://127.0.0.1:8000/api/schema/swagger-ui/)

>При запущенном сервере доступна интерактивная документация Swagger [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)


## Запуск приложения через Docker

Для локальной разработки бэкэнда(из **Cat_show**)

```bash
docker-compose -f docker-compose.yml --env-file ./settings/.env up -d --build
```
## Архитектура приложения

```
< PROJECT ROOT >
   |
   |--cats/
   |    |--migrations/
   |    |--models/
   |        |breed.py               #порода котят
   |        |cats.py                #котята
   |    |--serializers/
   |        |--breed_serializer.py  #сериализатор породы котят
   |        |--cat_serializer.py    #сериализатор котят
   |    |-- admin.py
   |    |-- apps.py
   |    |-- test.py
   |    |-- views.py
   |
   |-- config/                      # Настройки проекта              
       |-- settings.py
       |-- asgi.py
       |-- wsgi.py     
       |-- urls.py     
   |-- docs/                        #директория с документацией
   |    |--installation.md          #руководство по установке приложения
   |    |
   |-- filters/
   |    |breed_filter.py            #фильтрация по породе котенка
   |
   |-- users/
   |    |-- migrations/
   |    |-- models/
   |        |-- managers.py
   |        |-- users.py
   |    |-- admin.py
   |    |-- apps.py
   |    |-- serializers.py
   |    |-- test.py
   |    |-- urls.py
   |    |-- views.py
   |      
   |-- .env                         # файл с настройками проетка
   |-- .gitignore              
   |-- docker-compose.yml           # Docker             
   |-- Dockerfile                   # Docker
   |-- manage.py                    # точка входа Django 
   |-- poetry.lock                  # файл зависимостей приложения 
   |-- pyproject.toml               # файл зависимостей приложения 
   |-- README.md
   |-- start-web.sh                 # точка входа

```
