p = int(input("Enter proceeds: "))
c = int(input("Enter costs: "))
d = round((p - c) * 100 / p)
if p > c:

    print(f"Profit. Profitability of proceeds {d}%")
    n = int(input("Enter number of employees: "))
    print("Profit per one employeer", round((p - c)/n))
elif p == c:
    print("Zero")

else:
    print("Damage,", p - c)
