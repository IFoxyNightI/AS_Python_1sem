if __name__ == "__main__":
    pass
n = int(input("Введите натуральное число: "))
result = 0
for i in range(n + 1):
    term = ((-1) ** i) * (3 ** i)
    result += term
print(f"Сумма: {result}")
