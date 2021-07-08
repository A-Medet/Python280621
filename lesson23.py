my_dict = {1: 'Winter',2: 'Winter', 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer", 9: "Autumn", 10: "Autumn", 11: "Autumn", 12: 'Winter'}
month = int(input('Enter a number of month: '))
while month > 12 or month < 0:
    print("Error, please enter right month from 1 to 12!")
    break
print(my_dict.get(month))

