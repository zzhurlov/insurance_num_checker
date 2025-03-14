# Insurance Number Checker
Веб-приложение (Микросервис) для Пенсионного фонда Российской Федерации. Написано на Django.

# Стек технологий:
* Python
* Django
* Django REST Framework
* SQLite

# Описание:
Данное API предоставляет возможность проверить контрольную сумму СНИЛС, проверяет сущетсвует ли такой номер в базе данных и возвращает значения <СНИЛС> НАЙДЕН, НЕ НАЙДЕН (404), НЕКОРРЕКТНЫЙ СНИЛС (400)

# Требования:
* Python == >3.5
* asgiref==3.8.1
* attrs==25.3.0
* Django==5.1.7
* djangorestframework==3.15.2
* drf-spectacular==0.28.0
* inflection==0.5.1
* jsonschema==4.23.0
* jsonschema-specifications==2024.10.1
* PyYAML==6.0.2
* referencing==0.36.2
* rpds-py==0.23.1
* sqlparse==0.5.3
* typing_extensions==4.12.2
* uritemplate==4.1.1

# Запуск
В корне проекта пишем ```python manage.py runserver```
Переходим по эндпоинту /api/docs/  и тестим!

# Скриншоты API-шки
<img width="1307" alt="Снимок экрана 2025-03-14 в 16 35 47" src="https://github.com/user-attachments/assets/0b13e6ee-8cc3-468f-abe0-db9bb31bb048" />
<img width="1300" alt="Снимок экрана 2025-03-14 в 16 36 02" src="https://github.com/user-attachments/assets/0d73cb73-6485-43f5-aeda-72f0b3ea80f4" />

