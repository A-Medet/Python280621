a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

b = [el_ for el, el_ in zip(a, a[1:]) if el < el_]
print(b)