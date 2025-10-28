if __name__ == "__main__":
    pass
n = int(input("Введите кол-во элементов списка: "))
list = []
for i in range(n):
    element = int(input(f"Введите элемент {i + 1}: "))
    list.append(element)
positive_num = [x for x in list if x > 0]
positive_num.sort(reverse=True)
print(f"Положительные числа по убыванию: {positive_num}")
