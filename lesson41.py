from sys import argv

print("Выработка в часах: ", argv[1])
print("Ставка в час: ", argv[2])
print("Премия: ", argv[3])

print("Зарплата: ", int(argv[1]) * int(argv[2]) + int(argv[3]))