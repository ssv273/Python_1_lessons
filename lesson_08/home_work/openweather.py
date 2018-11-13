"""
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.

    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID,
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys

        Ключ имеет смысл сохранить в локальный файл, например, "app.id"


== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz

    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка
     (воспользоваться модулем gzip
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)

    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}


== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}


== Сохранение данных в локальную БД ==
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
import json
import os
import requests
import sqlite3


def tempr(real_temp, base_temp):
    if real_temp != base_temp:
        return True
    else:
        return False


path = os.path.join('data', 'city.list.json')
with open(path, 'r', encoding='utf-8') as fh:
    data_1 = json.load(fh)
# тут мы получили СПИСОК СЛОВАРЕЙ
# теперь попробуем вытащить список стран
country_list = []
for i in data_1:
    if i['country'] in country_list:
        pass
    else:
        country_list.append(i['country'])
# получили список стран, можем напечатать его по запросу

# так, теперь у нас есть список стран
# теперь попросим пользвателя ввести название города
city = input('Введите название города')
city = city.capitalize()
# так город мы ввели, теперь надо получить его ID
id_city = 0
flag = True
id_list = []
country_list1 = []
for i in data_1:
    if i['name'] == city:
        id_list.append(i['id'])
        country_list1.append(i['country'])
        flag = False
if flag:
    print('Имя не найдено')
# теперь нам надо уточнить выбор города, если их несколько
if len(country_list1) > 1:
    b = 1
    print('Город с таким именем найден в следующих странах: ')
    for el in country_list1:
        print('{}. страна - {}'.format(b, el))
        b += 1
    answer_city = int(input('Уточните пожалуйста в какой стране находится Ваш город введя цифру'))
    id_city = id_list[answer_city - 1]
else:
    id_city = id_list[0]
# теперь надо получить погоду для выбранного города
api_url = 'http://api.openweathermap.org/data/2.5/weather?'

my_app_id = '3c90583990e55c1d46f3312bb0f98d34'
data_list = {"id": id_city, "appid": my_app_id, "units": "metric"}
inquiry = requests.get(api_url, params=data_list)
data = inquiry.json()

# тааак, нам вернулся словарь
weather = [(data["id"], data["name"], data["dt"], data["main"]["temp"], data["weather"][0]["id"])]
temp = (weather[0][3])

# так, теперь попробуем создать БД


# f = os.path.isfile("mydatabase.db")
# if f = False:
#
conn = sqlite3.connect("mydatabase.db")
c = conn.cursor()
try:  # проверяем создана ли таблица
    c.execute(
        '''CREATE TABLE weather (id_города INTEGER PRIMARY KEY, Город VARCHAR(255), Дата DATE, Температура INTEGER, id_погоды INTEGER)''')
    conn.commit()
    c.executemany("INSERT INTO weather VALUES (?, ?, ?, ?, ?)", weather)
    conn.commit()

except:  # если создана, то
    try:
        # проверяем, есть ли запись с таким городом, если нет то создаем
        c.executemany("INSERT INTO weather VALUES (?, ?, ?, ?, ?)", weather)
        conn.commit()
    except:  # если есть, то проверяем температуру и изменяем запись, если она изменилась
        sql = "SELECT * FROM weather WHERE id_города=?"
        c.execute(sql, [(str(id_city))])
        s = c.fetchall()
        print(s)
        if tempr(temp, s[0][3]):
            print('Температура, зафиксированная в БД = {}, фактическа = {}, заменяем'.format(s[0][3], temp))
            c.execute(
                """REPLACE INTO weather (id_города, Город, Дата, Температура, id_погоды) VALUES (?, ?, ?, ?, ?)""",
                (data["id"], data['name'], data["dt"], data["main"]["temp"], data["weather"][0]["id"]))
            conn.commit()
sql_1 = "SELECT * FROM weather WHERE id_города=?"
c.execute(sql_1, [(str(id_city))])
s = c.fetchall()
print(s)
print('Эта запись добавлена в базу данных')
