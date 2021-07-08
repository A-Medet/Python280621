my_list = ['Winter', "Spring", "Summer", "Autumn", 'Winter']

while True:
    month = int(input('Enter a number of month: '))
    if 0 < month <= 12:
        print(my_list[month // 3])
        break
    else:
        print("Enter correct number of month from 1 to 12!")


