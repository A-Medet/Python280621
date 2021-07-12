# my_func = lambda num, degree: num ** degree
#
# print(my_func(float(input("Введите положительное число: ")), int(input("Введите целое отрицательное число: "))))

def my_func(x,y):
    try:
        x = float(x)
        y = int(y)

        if y >= 0 or x <= 0:
            print("Введите положительное число x и отрицательное у")
        else:
            involution = 1
            for el in range(-y):
                involution *= 1/x
            return f'Результат возведения x в степень у: {involution}'
    except (ZeroDivisionError, ValueError, TypeError):
        print("Введите корректные данные")

print(my_func(input("Введите положительное действительное число: "),input("Введите целое отрицательное число (показатель степени): ")))