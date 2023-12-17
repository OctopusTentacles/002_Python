# Задача 5. Web scraping

# Дан несложный пример HTML-страницы: examples.html (код загрузки текста 
# сайта из html файла добавлен в файл main.py)

# Изучите код этой страницы и реализуйте программу, которая получает 
# список всех подзаголовков сайта (они заключены в теги h3).

# Ожидаемый результат:

# ['Latest News', 'Useful Links', 'Search', 'Heading 3']
# Сделайте так, чтобы программа работала для любого сайта, где есть такие теги.

# Дополнительно: найдите любой сайт, у которого в коде есть теги 'h3', 
# выполните get-запрос к этому сайту при помощи библиотеки requests и 
# получите аналогичный список всех его подзаголовков (заключенных в теги 'h3')


import re
import os
import requests


# <h3>Latest News</h3>
cur_dir = os.path.dirname(__file__)


def search_text()

# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open(os.path.join(cur_dir, 'examples.html'), 'r') as f:
    text = f.read()
# По итогу вы так же получаете код сайта в виде одной строки

# .*? - любой символ от 0 и более раз
# (.*?) захват текста между тегами.
pattern = r"<h3.*?>(.*?)</h3>"
result = re.findall(pattern, text)
print(result)


response = requests.get("https://www.google.kz")
if response.status_code == 200:
    data = response.text


    print(data)