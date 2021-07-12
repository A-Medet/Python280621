def m_quontient(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Ошибка")

m_quontient(float(input("Введите делимое: ")), float(input("Введите делитель: ")))

# def m_quontient(a, b):
#     if b == 0:
#         print("Ошибка")
#     else:
#         print(a / b)
# m_quontient(float(input("Введите делимое: ")), float(input("Введите делитель: ")))

# def m_quontient():
#     a = float(input("Введите делимое: "))
#     b = float(input("Введите делитель: "))
#     if b == 0:
#         print("Ошибка")
#     else:
#         print(a / b)
# m_quontient()