def test_function():

    # Эта функция демонстрирует понятие пространства имен (области видимости).

    def inner_function():

        # Вложенная функция, доступная только внутри test_function.
        print("Я в области видимости функции test_function")

    inner_function()  # Вызов inner_function внутри test_function


test_function()  # Вызов test_function

try:
    inner_function() # Попытка вызова inner_function вне test_function
except NameError as e:
    print(f"Ошибка: {e} - inner_function не определена в этом пространстве имен.")