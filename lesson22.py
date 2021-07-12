my_str = input("Введите элементы списка через пробел: ")
my_list = my_str.split()
l = len(my_list)
for i in range(0, l - 1,2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)
