def sum_of_num():
    sum_num = 0
    while True:
        numbers = input("Для выхода из программы: q\nВведите числа через пробел: ")
        numbers = numbers.split()
        for number in numbers:
            if number == 'q':
                return sum_num
            else:
                try:
                    sum_num += float(number)
                except ValueError:
                    print("Чтобы остановить программу введите - q")
        print(sum_num)


print(sum_of_num())



