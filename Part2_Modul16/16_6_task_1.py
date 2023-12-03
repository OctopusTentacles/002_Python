# Задача 1. Права доступа
# Перед вами стоит задача создать и поддерживать специализированный форум. В
# Вы только приступили и сейчас работаете над действиями, которые могут совершать 
# посетители форума. Для разных пользователей прописаны разные возможности.

# Напишите декоратор check_permission, который проверяет, есть ли у пользователя 
# доступ к вызываемой функции, и если нет, то выдаёт исключение PermissionError.

# Результат:
# Удаляем сайт
# PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию add_comment

import functools


def check_permission(user: str):
    def permission(func):
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if user in user_permissions:
                    func(*args, **kwargs)
                    
                else:
                    raise PermissionError
            except PermissionError as exc:
                print(f"{exc.__class__.__name__}: у пользователя {user} недостаточно "
                      f"прав, чтобы выполнить функцию {func.__name__}")
                return
        return wrapper
    return permission

user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')

delete_site()
add_comment()