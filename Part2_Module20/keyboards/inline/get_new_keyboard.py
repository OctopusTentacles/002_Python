"""Модуль, содержащий функции для создания кнопок Telegram."""


from telebot import types


def get_new_keyboard():
    """Возвращает клавиатуру для выбора типа новинок.

    Returns:
        types.InlineKeyboardMarkup: Объект клавиатуры для новинок.
    """
    keyboard = types.InlineKeyboardMarkup()
    button0 = types.InlineKeyboardButton(text='Главное меню', callback_data='main')
    button1 = types.InlineKeyboardButton(text='Фильмы', callback_data='фильм')
    button2 = types.InlineKeyboardButton(text='Сериалы', callback_data='сериал')
    button3 = types.InlineKeyboardButton(text='Мультфильмы', callback_data='мульт')

    keyboard.add(button1, button2, button3, button0)
    return keyboard
