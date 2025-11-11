if __name__ == "__main__":
    pass
#a)
try:
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    print(a / b)
except ZeroDivisionError:
    print("Деление на ноль запрещено")
#б)
n = int(input("Введите число: "))
for i in range(2, n):
    if n % i == 0:
        raise Exception("Число не является простым")
print("Число является простым")
#в)
a = float(input("Первое число: "))
b = float(input("Второе число: "))
assert b != 0, "Деление на ноль запрещено"
print(a / b)
