# Тестовое задание

Стек:

<img src="https://img.shields.io/badge/Python-4169E1?style=for-the-badge"/> <img src="https://img.shields.io/badge/Django-008000?style=for-the-badge"/><img src="https://img.shields.io/badge/Docker-00BFFF?style=for-the-badge"/> <img src="https://img.shields.io/badge/PostgreSQL-87CEEB?style=for-the-badge"/> <img src="https://img.shields.io/static/v1?style=for-the-badge&message=Celery&color=37814A&logo=Celery&logoColor=FFFFFF&label"/> <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white"/> <img src="https://shields.io/badge/JavaScript-F7DF1E?logo=JavaScript&logoColor=000&style=flat-square"/> <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white">

# Описание проекта:

Этот проект представляет собой выполнение тестового задания от High Tech Academy. Он представляет собой простой сайт с
продажей интернет продуктов

Сайт обладает следующим функционалом:

- Покупка товаров
- Создание заказов
- Обработка заказов

# Как запустить проект

1. Клонировать репозиторий:

```
https://github.com/trixvlq/HTA.git
```

2. Перейти в директорию проекта:

```
cd Название папки на уровне файла docker-compose
```

3. В этой директории, а также в директории `core` нужно создать файл `.env` и задать в нём следующие значения:

```
DATABASE=база данных(database)
DBNAME=название базы данных
DBUSER=название юзера(service-user)
DBPASS=пароль базы данных
DBPORT=порт(5432)
EMAIL=Ваша почта
KEY=Пароль от smtp
HOME_EMAIL=Ваша почта
```

В зависимости от выбранного хоста будет необходимо ввести изменения в settings.py

4. Создать Docker контейнер:

```
docker-compose build
```

5. Создать админа:

```
docker-compose run --rm beer-app sh -c "python manage.py createsuperuser"
```

6. Запустить контейнер:

```
docker-compose up
```

Теперь проект доступен по адресу:

```
http://127.0.0.1/
```

Необходимо будет создать модели продуктов для работы на сайте, это делается по следующему урлу

```commandline
http://127.0.0.1/admin/
```

## Автор

- Имя: Цзю Максим
- Email: qwefghnz@gmail.com
- GitHub: [trixvlq](https://github.com/trixvlq)