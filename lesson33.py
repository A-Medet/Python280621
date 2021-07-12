def my_func(a, b, c):
    """Функция выдает наибольщую сумму двух чисел, путем исключения наименьшего из них"""
    if a < b or a < c:
        print(b + c)
    elif b < c:
        print(a + c)
    else:
        print(a + b)
my_func(float(input("Введите первое число: ")), float(input("Введите второе число: ")), float(input("Введите третье число: ")))