def foo(x):
    if x == 0:
        print("Вызов foo(0) возвращает 0")
        return 0
    else:
        print(f"Вызов foo({x - 1}) начинается и добавляется в стек")
        new_result = foo(x - 1)
        print(f"Вызов foo({x - 1}) завершился и удаляется из стека")
        result = x + new_result
        return result

print(f"Вызов foo(2) начинается и добавляется в стек")
result = foo(2)
print(f"Вызов foo(2) завершается и удаляется из стека")
print("Итоговый ответ — ", result)