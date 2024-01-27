"""Модуль, содержащий функции для создания кнопок Telegram."""


from telebot import types


def get_main_keyboard():
    """Возвращает основную клавиатуру.

    Returns:
        types.InlineKeyboardMarkup: Объект основной клавиатуры.
    """
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Новинки', callback_data='новинки')
    button2 = types.InlineKeyboardButton(text='Топ', callback_data='топ')
    button3 = types.InlineKeyboardButton(text='Рандом', callback_data='random')
    button4 = types.InlineKeyboardButton(text='Поиск фильма', callback_data='search_movie')
    button5 = types.InlineKeyboardButton(text='Поиск актера', callback_data='search_person')
    button6 = types.InlineKeyboardButton(text='История', callback_data='history')

    keyboard.add(button1, button2, button3, button4, button5, button6)
    return keyboard


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
