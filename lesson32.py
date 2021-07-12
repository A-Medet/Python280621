def info(**kwargs):
    return kwargs

print(info(name=input("Введите Имя: "), surname=input("Введите Фамилию: "), birth_year=input("год рождения: "), residence=input("город проживания: "), email=input("email: "), telephone=input("телефон: ")))

# f_name = input("Введите Имя: ")
# s_name = input("Введите Фамилию: ")
# birth_year = int(input("год рождения: "))
# residence = input("город проживания: ")
# e_mail = input("email: ")
# phone_num = input("телефон: ")

# f"Данные пользователя: {f_name} {s_name}. Год рождения: {birth_year}, город проживания: {residence}, email: {e_mail}, телефон: {phone_num}"