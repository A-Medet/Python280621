n = int(input('Сколько товаров вы хотите добавить: '))
i = 0
while i < n:
    my_str = input("Введите через пробел характеристики следующего товара: название, цена, количество, единица измерения: ")
    my_list = my_str.split()
    my_tuple = (i+1, {'название': my_list[0], "цена": my_list[1], "количество": my_list[2], "ед": my_list[3]})

    i += 1
    print(my_tuple)







# n = int(input('Сколько товаров вы хотите добавить: '))
# my_str = input("Введите названия товаров через пробел: ")
# my_list = my_str.split()
# i = 1
# while i <= n:
#     my_tuple = (i, {'название': my_list[i-1]})
#     i += 1
#     print(my_tuple)

