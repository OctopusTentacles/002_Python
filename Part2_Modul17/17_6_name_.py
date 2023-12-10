# Специальная переменная __name__


import test_module


if __name__ == "__main__":
    print("Инициализирую исполняемый файл")
    test_module.func()