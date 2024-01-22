from telebot import TeleBot, types
from telebot.types import CallbackQuery, Message

bot = TeleBot('YOUR_BOT_TOKEN')

user_responses = {}  # Словарь для хранения ответов пользователей

@bot.callback_query_handler(func=lambda call: call.data == 'search_movie')
def get_search_movie(call: CallbackQuery):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    user_name = call.from_user.first_name

    print(chat_id, user_id, user_name)

    bot.send_message(chat_id, f'{user_name}! Введи название фильма:')
    bot.register_next_step_handler(call.message, lambda message: save_user_input(message, user_id))

def save_user_input(message: Message, user_id: str):
    chat_id = message.chat.id
    user_responses[user_id] = message.text.strip()

    # Теперь user_responses содержит ответ пользователя, соответствующий user_id
    print(f'User {user_id} entered: {user_responses[user_id]}')

if __name__ == '__main__':
    bot.polling(none_stop=True)









# import requests
# import telebot

# from io import BytesIO

# from telebot import TeleBot
# from telebot.types import CallbackQuery


# from buttons import get_main_keyboard
# from buttons import get_new_keyboard
# from logger import logger
# from models import UserRequest

# # from config import API_KEY
# # from config import BOT_TOKEN


# user_response = {}


# def get_search_movie(bot: TeleBot, call: CallbackQuery,
#                  user_name: str, user_id: str):
        

#         bot.send_message(
#              call.message.chat.id,
#              f'Введи название фильма'
#         )

#         print(1)

#         bot.register_next_step_handler(call.message.from_user.id, user_input_title)
        
#         logger.info(f'Отправлен запрос от бота для выбора типа контента '
#                     f'пользователю {call.from_user.id}.'
#         )
#         print(2)

# def user_input_title(message):
#     """Функция срабатывает автоматически при отправке текстового сообщения"""

#     print(3)

#     chat_id = message.chat.id

#     user_response[chat_id] = message.text.strip()
#     print(user_response[chat_id])

#     print(4)

#     create_url(message)

# def create_url(chat_id):
#     # Получаем введенное пользователем название фильма
#     query = user_response.get(chat_id, '')

#     print(5)

#     url = (
#         f'https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=1&'
#         f'query={query}'
#     )

#     print('ссылка поиска', query)


# # if __name__ == '__main__':
# #     bot.infinity_polling()
