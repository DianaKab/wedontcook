# Wedontcook

## Описание проекта:
### Телеграмм-бот для заказа тортиков.
Это телеграмм-бот предназначен для принятия заказов тортиков. Происходит расчет стоимости заказа по запросу покупателя. 
По выбранным категориям: декор, вес торта, тип торта и вкуса формируется заказ и его стоимость.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:DianaKab/wedontcook.git
```

```
cd wedontcook
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```
В Windows:
```
source venv/Scripts/activate
```
В macOS или Linux:
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры работы телеграмм-бота:

Чтобы разбудить бот 

```
/start
```
Далее бот приветсвует пользователя по нику в Телеграм.

```
Здравствуйте, Diana, мы рады, что вы хотите заказать у нас тортик!
```
```
Какой вкус торта, вы хотите заказать? 
Выберите из: морковный/ванильный/шоколадный
```
Далее выбор типа торта
```
Какой тип торта вы хотите заказать? 
(выберите из: бенто/по весу)
```
Далее выбор декора торта
```
Круто! Теперь выберите декор для торта? 
(Выберите из: с ягодами/с цветами/с надписью)
```
Далее пользователь должен написать дату заказа
```
Классс! Теперь скажите дату вашего заказа.
Напишите в формате - день-месяц (Пример 11-ноября)
```
Формируется заказ и отправляется сообщение с расчетом стоимости заказа.
```
Ваш заказ:
Вкус - морковный
Тип торта - бенто
Декор - с надписью
Стоимость вашего заказа - 1300
```
В случае некорректных ответов, бот отправляет сообщение о неточностях.
Например:
```
Ой, такого декора нет. Выберите из предложенных: с ягодами/с цветами/с надписью.
```
