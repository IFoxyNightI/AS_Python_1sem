if __name__ == "__main__":
    pass
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
if A >= B:
    print("Ошибка - A должно быть меньше B")
else:
    for i in range(B-1, A, -1):
        print(i)
    N = B - A - 1
    print(f"Количество чисел = {N}")
