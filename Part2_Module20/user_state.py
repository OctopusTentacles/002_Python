"""Машина состояний пользователя."""


import wrapt


def user_state(wrapped, instance, args, kwargs):
    """Декоратор для управления состояниями пользователей в боте Telegram.

    Args:
        wrapped: Оригинальная функция для обертывания.
        instance: Экземпляр класса Telebot, обрабатывающий сообщение.
        args: Позиционные аргументы, переданные в оригинальную функцию.
        kwargs: Именованные аргументы, переданные в оригинальную функцию.

    Returns:
        Результат выполнения оригинальной функции.
    """

    # получаем ID пользователя из сообщения:
    user_id = instance.from_user.id

    # Получение атрибута user_states из экземпляра класса. 
    # Если атрибут не существует, используется пустой словарь.
    instance.user_states = getattr(instance, 'user_states', {})

    # Получение состояния пользователя из словаря user_states. 
    # Если состояние пользователя не существует, 
    # используется пустой словарь.
    instance.user_states[user_id] = getattr(
        instance, 'user_states', {}
    ).get(user_id, {})

    # Установка категории состояния пользователя. 
    # используем значение "start", если категория не была 
    # передана в виде аргумента.
    instance.user_states[user_id]['category'] = kwargs.get('caategory', 'start')

    return wrapped(*args, **kwargs)