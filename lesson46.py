from sys import argv
from itertools import count, cycle

a = int(argv[1])
for i in count(a):
    if i == int(argv[2]):
        break
    print(i)

num = 0
b = argv[3]
for i in cycle(b):
    if num == 10:
        break
    print(i)
    num += 1