# Документация
Документация api:


```
http://localhost:8000/docs
```

# Тесты


```
\tests
```


Запуск тестов:

```
pytest
```

# Запуск проекта

1. Клонируйте репозиторий:

```
https://github.com/iMaanick/form-api.git
```

2. При необходимости установить Poetry ```pip install poetry```

3. Запустить виртуальное окружение ```poetry shell```

4. Установить зависимости ```poetry install```


5. Добавьте файл .env и заполните его как в примере .example.env:

```
DATABASE_URI=sqlite+aiosqlite:///test.db
DB_PATH=db.json
```
6. Выполните для создания таблиц

```
alembic upgrade head 
```

7. Для заполнения тестовыми данными выполните:
```
python -m app.main.test
```
8. Для запуска c tinydb выполните:
```
uvicorn --factory app.main:create_nosql_app --host localhost --port 8000
```
9. Для запуска c sqlite выполните:
```
uvicorn --factory app.main:create_sql_app --host localhost --port 8000
```

# Функциональность

В качестве дополнения к основному заданию реализован SQL-адаптер для работы с базой данных. Для запуска с ним см. пункт 9   

Шаблон формы — структура с уникальным набором полей и указанием их типов:
```json
{
    "name": "Form template name",
    "field_name_1": "email@mail.ru",
    "field_name_2": "+79111111111"
}
```
Типы данных полей:

 - email
 - phone (+7xxxxxxxxxx)
 - date (DD.MM.YYYY или YYYY-MM-DD)
 - text

Логика поиска формы:

- Поля шаблона должны совпадать по имени и типу с переданными в форме.

- Дополнительные поля не мешают совпадению.

Ответы API:

- Совпадение найдено: возвращается список из совпавших имен шаблонов (их может быть более одного).
- Совпадение не найдено: возвращается список полей с определенными типами

```json
{
    "field_name_1": "email",
    "field_name_2": "text"
}
```

API

POST `/get_form` (да, именно post)

Входные данные:

Список полей со значениями в теле POST запроса.

Пример:

Request body:

```json
{
    "Email Address": "user1@example.com",
    "Phone Number": "+71234567890",
    "Birth Date": "2000-01-01"
}
```
Выходные данные:

- Список из совпавших имен шаблонов
- При отсутствии совпадений: типизированные поля.

Пример:

Response body:

```json
{
  "Email Address": "email",
  "Phone Number": "phone",
  "Birth Date": "date"
}
```

или

```json
[
  {
    "name": "Registration Form"
  }
]
```

# О проекте
1. FastAPI для разработки REST API
2. SQLite и tinydb в качестве базы данных
3. SQLAlchemy для работы с SQLite
4. aiotinydb для работы с tinydb
5. Alembic для управления миграциями
6. Pytest для тестов
7. Poetry для управления зависимостями