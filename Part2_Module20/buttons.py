from telebot import types


def get_main_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Новинки', callback_data='новинки')
    button2 = types.InlineKeyboardButton(text='Случайный фильм', callback_data='рандом')
    button3 = types.InlineKeyboardButton(text='История', callback_data='history')
    
    keyboard.add(button1, button2, button3)
    return keyboard


def get_new_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button0 = types.InlineKeyboardButton(text='Главное меню', callback_data='main')
    button1 = types.InlineKeyboardButton(text='Фильмы', callback_data='фильм')
    button2 = types.InlineKeyboardButton(text='Сериалы', callback_data='сериал')
    button3 = types.InlineKeyboardButton(text='Мультфильмы', callback_data='мульт')
    
    keyboard.add(button1, button2, button3, button0)
    return keyboard
