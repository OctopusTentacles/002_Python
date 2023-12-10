def func() -> None:
    print("Я функция func() из test_module")


if __name__ == "__main__":
    print("Тут есть основной код")
    func()
else:
    print("Импортирован модуль", __name__)