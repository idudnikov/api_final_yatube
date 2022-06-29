<h2 align="center">API портала Yatube</h2>

Данный проект представляет собой API портала Yatube. Он позволяет работать с данными портала Yatube (получать, создавать, изменять и удалять) через API.  

## Установка и использование

### Установка

Клонируйте файлы проекта в локальное хранилище и перейдите в папку с проектом:

`git clone https://github.com/idudnikov/api_final_yatube.git`

`cd api_final_yatube`

Создайте и активируйте виртуальное окружение:

`python3 -m venv venv`

`source env/bin/activate`

Установите зависимости:

`python3 -m pip install --upgrade pip`

`pip install -r requirements.txt`

Выполните миграции:

`python3 manage.py migrate`

Запустите проект:

`python3 manage.py runserver`

### Использование

Проект поддерживает следующие эндпоинты и методы запроса:

1. `/api/v1/posts/`

GET - получение публикаций, POST - создание новой публикации

2. `/api/v1/posts/{id}/`

GET - получение публикации, PUT - обновление публикации, PATCH - частичное обновление публикации, DELETE - удаление публикации

3. `/api/v1/posts/{post_id}/comments/`

GET - получение комментариев, POST - создание нового комментария

4. `/api/v1/posts/{post_id}/comments/{id}/`

GET - получение комментария, PUT - обновление комментария, PATCH - частичное обновление комментария, DELETE - удаление комментария

5. `/api/v1/groups/`

GET - получение списка групп

6. `/api/v1/groups/{id}/`

GET - получение информации о группе

7. `/api/v1/follow/`

GET - получение информации о подписках, POST - подписка на автора

8. `/api/v1/jwt/create/`

POST - создание JWT токена

9. `/api/v1/jwt/refresh/`

POST - обновление JWT токена

10. `/api/v1/jwt/verify/`

POST - проверка JWT токена
