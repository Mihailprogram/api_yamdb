# api_yamdb
REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке. (Совместный проект 3 студентов Яндекс Практикум)
# Описание 
API для сервиса YaMDb. Позволяет работать со следующими сущностями:

JWT-токен (Отправление confirmation_code на переданный email, получение JWT-токена в обмен на email и confirmation_code)

Пользователи (Получить список всех пользователей, создание пользователя, получить пользователя по username, изменить данные пользователя по username, удалить пользователя по username, получить данные своей учетной записи, изменить данные своей учетной записи)

Категории (типы) произведений (Получить список всех категорий, создать категорию, удалить категорию)

Категории жанров (Получить список всех жанров, создать жанр, удалить жанр)

Произведения, к которым пишут отзывы (Получить список всех объектов, создать произведение для отзывов, информация об объекте, обновить информацию об объекте, удалить произведение)

Отзывы (Получить список всех отзывов, создать новый отзыв, получить отзыв по id, частично обновить отзыв по id, удалить отзыв по id)

Коментарии к отзывам (Получить список всех комментариев к отзыву по id, создать новый комментарий для отзыва, получить комментарий для отзыва по id, частично обновить комментарий к отзыву по id, удалить комментарий к отзыву по id)

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Mihailprogram/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
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
Если есть необходимость, заполняем базу тестовыми данными командой:
```
python manage.py load_data
```
Для повторного использования нужно удалять данные из БД, иначе выпадут ошибки 
Unique constraint failed
# Участники 
Activishion - управление пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения e-mail, поля.

avolodin532 - категории (Categories), жанры (Genres) и произведения (Titles): модели, view и эндпойнты для них.

Mihailprogram - отзывы (Review) и комментарии (Comments): модели и view, эндпойнты, права доступа для запросов. Рейтинги произведений.