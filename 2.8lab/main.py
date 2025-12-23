if __name__ == "__main__":
    pass
import math

# Создаем файл с числами
with open('f.txt', 'w') as f:
    f.write("4\n7\n9\n15\n16\n25\n36\n50\n64\n81\n100\n121\n144\n169\n200")

# Читаем числа, находим квадраты, записываем результат
with open('f.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f if line.strip()]

perfect_squares = []
for num in numbers:
    root = int(math.sqrt(num))
    if root * root == num:
        perfect_squares.append(num)

with open('g.txt', 'w') as g:
    for square in perfect_squares:
        g.write(f"{square}\n")

# Выводим результаты
print("Числа из f.txt:", numbers)
print("Точные квадраты:", perfect_squares)
print("Результат записан в g.txt")
