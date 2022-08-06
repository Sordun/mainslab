## Тестовое для mainslab.ai

```
Используя Django REST framework создать:

1. эндпоинт для обработки файла bills.xlsx

В базу писать только валидные счета. Счет считается валидным, если выполнены все условия:
* значение sum является числом
* в service не пусто ( пусто так же считается, если вместо текста знак “-”)
* корректная дата (дата считается корректной, если есть день, месяц и год).
* №(номер счет) тип  int
* client_name, client_org не пустые

2. эндпоинт со списком счетов с возможностью фильтровать по организации, клиенту.
```

#### 1. Применение миграций:

```bash
python manage.py migrate
```

#### 2. Запуск проекрта:

```bash
python manage.py runserver
```

Проект доступен по адресу http://127.0.0.1:8000
1) для загрузки http://127.0.0.1:8000/upload/bills/
2) для просмотра http://127.0.0.1:8000/bills/