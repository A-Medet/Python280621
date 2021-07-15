from functools import reduce

a = [i for i in range(100, 1001, 2)]
def m_production(first, second):
    return first * second
result = reduce(m_production, a)
print(f'Произведение всех четных чисел от 100 до 1000: {result}')