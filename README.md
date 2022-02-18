# api_final
API проекта Yatube (v1).


### Установка:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/sofyaserpinskaya/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры:

Получить список всех публикаций:

```
GET /api/v1/posts/
```

Добавление новой публикации в коллекцию публикаций:

```
POST /api/v1/posts/
```

Обновление публикации по id:

```
PUT /api/v1/posts/{id}/
```

Добавление нового комментария к публикации:

```
POST /api/v1/posts/{post_id}/comments/
```

Удаление комментария к публикации по id:

```
DELETE /api/v1/posts/{post_id}/comments/{id}/
```

Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса:

```
POST /api/v1/follow/
```
