n = int(input("Enter time in seconds: "))
a = n // 3600
b = (n - 3600 * a) // 60
c = n - 3600 * a - 60 * b
print(f"{a:02}:{b:02}:{c:02}")
