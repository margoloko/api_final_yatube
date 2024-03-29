api final yatube 
## Проект api_yatube - это API социальной сети yatube.

С помощью api_yatube можно запрашивать данные о постах, группах, комментариях в социальной сети Yatube, а также создавать новые.


### Установка:

Склонируйте репозиторий:

```
git clone https://github.com/margoloko/api_final_yatube.git
```

Активируйте виртуальное окружение и установите зависимости из файла requirements.txt:

```
python -m pip install
```
```
pip install -r requirements.txt
```

Выполните миграции:

```
python manage.py migrate
```

Запустите проект:

```
python manage.py runserver
```

### Примеры использования:

Получить список всех постов:

```
GET /api/v1/posts/
```

Добавление нового поста:

```
POST /api/v1/posts/
```
Получить список всех групп:

```
GET /api/v1/groups/
```

Добавление нового комментария:

```
POST /api/v1/posts/{post_id}/comments/
```

Удаление комментария по id:

```
DELETE /api/v1/posts/{post_id}/comments/{id}/
```
Получение списока подписок:

```
GET /api/v1/follow/
```

Подписка пользователя на пользователя переданного в запросе:

```
POST /api/v1/follow/
```
### Используемые технологии:
- Python
- Django
- DRF
- JWT + Djoser

### Author:
[Balakhonova Marina](https://github.com/margoloko)
