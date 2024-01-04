import telebot
from config import BOT_TOKEN
from buttons import get_main_keyboard, get_new_keyboard
from new import get_new_url


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):
    username = message.from_user.first_name
    keyboard = get_main_keyboard()
    bot.send_message(message.chat.id, f"Привет, {username}!\n"
                     f"Выбери одну из команд:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def main_menu(call):

    category = None
    if call.data == "новинки":
        ask_user_buttons(call)
    elif call.data in ["фильм", "сериал", "мульт"]:
        category = call.data

    if category is not None:
        get_new_url(call.message.chat.id, category)


def ask_user_buttons(call):
    keyboard = get_new_keyboard()
    bot.send_message(call.message.chat.id, "Выбери тип", reply_markup=keyboard)


if __name__ == "__main__":
    bot.infinity_polling()
