if __name__ == "__main__":
    pass
N = int(input("Введите кол-во элементов списка: "))
print("Введите элементы списка: ")
my_list = []
for i in range(N):
    element = int(input(f"Элемент {i + 1}: "))
    my_list.append(element)
K = int(input("Введите число K: "))
L = int(input("Введите число L: "))
if not (1 < K <= L <= N) :
    print("Ошибка: должно выполняться условие: 1<K≤L≤N")
else:
    total_sum = 0
    count = 0
    for i in range(N):
        if i + 1 < K or i + 1 > L:
            total_sum += my_list[i]
            count += 1
average = total_sum / count if count > 0 else 0
print(f"Среднее арифметическое: {average: .2f}")
