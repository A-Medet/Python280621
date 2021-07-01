s = int(input('Введите натуральное число: '))
max_num = s % 10
num = s

while num > 0:
    m = num % 10
    if max_num < m:
        max_num = m
    num = num // 10

print(max_num)

