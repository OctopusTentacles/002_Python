# Работа с API

# API (англ. Application Programming Interface — программный интерфейс приложения) — 
# набор способов и правил, по которым различные программы общаются между собой и 
# обмениваются данными.

# API
# https://yandex.ru/dev/
# https://publicapis.dev


# Получаем API-ключ
# Попробуем повзаимодействовать с одним из них. Возьмём API «Яндекс Словаря». 
# Для начала нужно получить бесплатный ключ на странице сервиса.
# https://yandex.ru/dev/dictionary/

# Делаем пробные запросы
# Перейдя по ссылке ниже, вы можете увидеть JSON со списком доступных направлений перевода:
# https://dictionary.yandex.net/api/v1/dicservice.json/getLangs?key=ВАШ_API_КЛЮЧ

# Посмотрим, что с этим можно сделать в методе lookup. Здесь необходимо вводить 
# дополнительные параметры: направление перевода и текст. 
# Также есть необязательные: язык интерфейса и опции поиска.
# Возьмём слово «задача» и направление ru-en. Вставим их в URL-параметры:
# https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=ВАШ_API_КЛЮЧ&lang=ru-en&text=задача
# В ответ получим различные переводы и синонимы. Проделайте то же самое у себя в браузере.

# Делаем запросы с помощью requests
# Сделаем то же самое, только с помощью Python. Для начала установим модуль 
# requests — он понадобится для отправки запросов:

# pip install requests
import requests
from pprint import pprint

API_KEY = 'ВАШ_API_КЛЮЧ'
BASE_URL = 'https://dictionary.yandex.net/api/v1/dicservice.json'

def get_langs():
    response = requests.get(f'{BASE_URL}/getLangs', params={
        'key': API_KEY
    })
    return response

def lookup(lang, text, ui='ru'):
    response = requests.get(f'{BASE_URL}/lookup', params={
        'key': API_KEY,
        'lang': lang,
        'text': text,
        'ui': ui
    })
    return response

langs_response = get_langs()
if langs_response.status_code != 200:
    print('Не удалось получить список направлений перевода')
    exit(1)

langs = langs_response.json()
print('Выберите одно из доступных направлений перевода')
print(langs)
while (lang := input('Введите направление: ')) not in langs:
    print('Такого направления нет. Попробуйте ещё раз')

text = input('Введите слово или фразу для перевода: ')
lookup_response = lookup(lang, text)
if lookup_response.status_code != 200:
    print('Не удалось выполнить перевод:', lookup_response.text)
    exit(1)

pprint(lookup_response.json())

# На что стоит обратить внимание
# BASE_URL — часть ссылки, которая не меняется при обращениях к этому API.
# Запрос делается с помощью requests.get, где первый аргумент — это ссылка, 
# а дальше мы указываем URL-параметры, передав их в params.p

#  сырой ссылке URL-параметры выглядят так:
# ?key=ВАШ_API_КЛЮЧ&lang=ru-en&text=задача
# В принципе, если вставить их в код таким образом, он всё равно сработает.

# В виде словаря код выглядит так:

params = {
    'key': 'ВАШ_API_КЛЮЧ', 
    'lang': 'ru-en', 
    'text': 'задача'
}

# Использование словаря повысит читаемость кода, поэтому этот способ предпочтительный.

# Ещё есть requests.post, который посылает POST-запрос.
# Если GET-запрос предназначен для получения информации от сервера, 
# то POST — больше для передачи информации серверу. Применяйте тот или иной метод 
# в зависимости от документации.
# Методы requests.get и requests.post возвращают объект ответа, 
# который содержит в себе код (2xx — успешные запросы, 4xx — неправильные запросы, 
# 5xx — ошибки сервера), а также текст. Если обращаемся в формате JSON, 
# можно сразу получить его с помощью response.json().

# В API некоторые данные могут передаваться в заголовках или теле запроса:
requests.post(url, headers={}, data={})

# Часто в API указывают ключ в заголовке:
requests.post(url, headers={
    'X-RapidAPI-Key': 'ВАШ_API_КЛЮЧ',
    'X-RapidAPI-Host': 'hotels4.p.rapidapi.com'
}, data={
    'currency': 'USD'
})
# У всех API разный контракт взаимодействия, поэтому тщательно изучайте документацию.

# =======================================================================================
# Интеграция API в телеграм-бот

# config.py — объявление токенов, ключей и прочих констант;
# states.py — объявление состояний пользователя;
# api.py — работа с API;
# main.py — создание обработчиков и запуск бота.
# В идеале в main.py нужно оставить только запуск бота, 
# а обработчики вынести в отдельный модуль.

# Конфигурационный файл
# При работе в PyCharm нужно было бы создать файл .env и загрузить его в 
# переменные программы с помощью библиотеки python-dotenv.

# Состояния
# У нас всего три состояния:
# base — пользователь просто находится в главном меню;
# lang — пользователь выбирает направление перевода;
# lookup — пользователь ищет слово или фразу.

# =======================================================================================
# Работа с API
# Здесь максимально простой интерфейс: функции делают запрос и возвращают обычные 
# словари или списки, которые отдал сервер.

# Обычно в ответе сервера есть много лишней информации, поэтому отсеивать её 
# лучше прямо в модуле api.py, например создав класс вида LookupResult, 
# который в более удобном виде будет хранить списки синонимов и переводов.

# =======================================================================================
# Основная логика телеграм-бота
# Так как у нас не меняются доступные языки, мы можем запросить их сразу на старте 
# работы. Это повысит производительность, потому что не нужно будет ждать 
# ответа от сервера.

# Из команды /start мы переходим в базовое состояние base.

# При вводе команды /set_lang переходим в состояние lang. По умолчанию направление 
# перевода — ru-en. Меняем выбранное направление и читаем текст с помощью метода 
# retrieve_data. После выбора языка идём обратно в состояние base.

# При вводе команды /lookup переходим в состояние lookup. После поиска 
# возвращаемся в base.
# Здесь мы схалтурили и сразу вывели словарь, который отдал нам сервер. 
# Пользователю может быть неудобен такой вариант, так как не все пользователи — 
# программисты, поэтому лучше преподнести это в более читаемом виде, дополнительно 
# обработав данные. Чтобы красиво вывести такой словарь, мы воспользуемся 
# двумя фишками:
# json.dumps сделает отступы.
# parse_mode='html' позволит использовать HTML-разметку. Тег <pre> как раз обычно 
# используется для подобных данных.
# С помощью set_my_commands мы зададим основные команды, 
# к которым пользователь может обратиться. 


# Выводы

# Выделим важные моменты, которые стоит помнить при разработке телеграм-бота.

# Пользователь не знает, как работает ваш бот, поэтому всегда необходимо 
# объяснять ему, что чат-бот собой представляет, а также давать наводки на следующие 
# действия и всячески помогать принимать решения.

# Построение архитектуры — залог качественной технической реализации телеграм-бота. 
# Выносите независимые блоки в отдельные модули.

# Скрывайте свои секретные данные с помощью переменных окружения.
# Для навигации пользователя в боте рекомендуется использовать конечный автомат 
# состояний.
# Кнопки помогают направить пользователя и посоветовать ему, как поступить на 
# том или ином этапе.
# Обращайте внимание на порядок объявления обработчиков. 
# Например, если первый обрабатывает все сообщения (func=lambda m: True), 
# а второй — команду /hello, то при написании /hello отработает именно первый 
# обработчик, потому что он объявлен раньше.
# Библиотека requests позволяет работать с внешними API. 
# Прежде чем использовать такой API, ознакомьтесь с документацией сервиса, 
# чтобы не допустить ошибок. Обратите внимание на метод (GET/POST/DELETE/PUT), 
# заголовки, параметры и тело запроса.