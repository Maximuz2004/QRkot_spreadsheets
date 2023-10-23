# Приложение QRKot

## Описание проекта
QRKot - это приложение для благотворительного фонда поддержки котиков.
Фонд собирает пожертвования на различные целевые проекты: на медицинское 
обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в 
подвале, на корм оставшимся без попечения кошкам — на любые цели, 
связанные с поддержкой кошачьей популяции.


Ключевые возможности сервиса:
- __Проекты.__ В приложении QRKot может быть открыто несколько целевых 
проектов. У каждого проекта есть название, описание и сумма, которую 
планируется собрать. После того, как нужная сумма собрана — проект закрывается.
- __Пожертвования.__ Каждый пользователь может сделать пожертвование и 
сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а 
не в конкретный проект. Каждое полученное пожертвование автоматически 
 добавляется в первый открытый проект, который ещё не набрал нужную сумму. 
Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — 
оставшиеся деньги ждут открытия следующего проекта. При создании нового 
проекта все неинвестированные пожертвования автоматически вкладываются в 
новый проект.
- __Пользователи__. Целевые проекты создаются администраторами сайта. 
Любой пользователь может видеть список всех проектов, включая требуемые и уже 
внесенные суммы. Это касается всех проектов — и открытых, и закрытых.
Зарегистрированные пользователи могут отправлять пожертвования и просматривать
список своих пожертвований.
- __Отчеты__. У администратора проекта имеется возможность формирования отчёта 
в гугл-таблице. В таблице указаны закрытые проекты, отсортированные по 
скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что
долго собирали нужную сумму.

## Стек технологий:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![FastApi](https://img.shields.io/badge/-Fastapi-464646?logo=fastapi)](https://fastapi.tiangolo.com/)
[![FastApi-SQLAlchemy](https://img.shields.io/badge/-FastapiSQLAlchemy-464646?logo=fastapi)](https://fastapi.tiangolo.com/how-to/async-sql-encode-databases/?h=sqlalchemy#import-and-set-up-sqlalchemy)
[![Fastapi-Users](https://img.shields.io/badge/-Fastapi_Users-464646?logo=fastapi)](https://fastapi-users.github.io/fastapi-users/10.0/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?logo=Pydantic)](https://docs.pydantic.dev/latest/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?logo=alembic)](https://alembic.sqlalchemy.org/en/latest/)
[![aioGoogle](https://img.shields.io/badge/-aioGoogle-464646?logo=aioGoogle)](https://alembic.sqlalchemy.org/en/latest/)
## Документация API проекта

Документация API проекта доступена по адресам:
- [Документация (Swagger)](http://127.0.0.1:8000/docs#)
- [Документация (Redoc)](http://127.0.0.1:8000/redoc#)

## Установка и запуск:
Клонировать репозиторий и перейти в него в командной строке:


```
git clone git@github.com:Maximuz2004/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
### Использование :
Создайте проект в Google Cloud Platform
Подключите к проекту необходимые API - Google Drive API и Google Sheets API.
Создайте сервисный аккаунт и получите JSON-файл с ключом доступа к нему.
Создайте удобным для вас способом в корневой директории проекта
файл ```.env``` с содержимым:
```
APP_TITLE=Кошачий благотворительный фонд
APP_DESCRIPTION=Сервис для поддержки котиков!
DATABASE_URL=sqlite+aiosqlite:///./charity_project_donation.db
SECRET=Some secret word
EMAIL= # Ваш адрес почты аккаунта google
# Далее указываем данные из JSON-файла вашего сервисного аккаунта:
TYPE=service_account
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=
UNIVERSE_DOMAIN=
```
Значение секретного ключа ```SECRET``` можете установить на свое
усмотрение.

Далее создаем базу данных:

```
alembic upgrade head
```

Далее запустите проект в терминале командой:
```
uvicorn app.main:app
```
Проект будет доступен по адресу: [http://127.0.0.1:8000/]( http://127.0.0.1:8000/)


Примеры запросов к API, указаны в документации по ссылкам выше.

Автор: [Титов Максим](https://github.com/Maximuz2004)