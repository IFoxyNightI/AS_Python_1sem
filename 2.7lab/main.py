if __name__ == "__main__":
    pass
def remove_first_k_chars_simple(input_file: str, k: int, output_file: str = None):
    """
    Args:
        input_file: имя входного файла
        k: количество символов для удаления
        output_file: имя выходного файла (если None, создается 'output.txt')
    """
    if k <= 0:
        raise ValueError("K должно быть положительным числом")

    output_file = output_file or "output.txt"

    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in lines:
                # Если строка длиннее K, удаляем K символов, иначе оставляем пустую строку
                if len(line) > k:
                    # Сохраняем перевод строки, если он был
                    if line.endswith('\n'):
                        outfile.write(line[k:])
                    else:
                        outfile.write(line[k:] + '\n')
                else:
                    # Для строк короче K записываем только перевод строки, если он был
                    if line.endswith('\n'):
                        outfile.write('\n')

        print(f"Файл обработан. Результат сохранен в '{output_file}'")

    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден")

# Пример
if __name__ == "__main__":
    
    input_filename = "example.txt"
    k_value = 5

    # Создаем файл
    with open(input_filename, 'w', encoding='utf-8') as f:
        f.write("Hello World!\n")
        f.write("Test line\n")
        f.write("Short\n")
        f.write("A very long line of text for demonstration purposes.\n")

    print("Исходный файл:")
    with open(input_filename, 'r', encoding='utf-8') as f:
        print(f.read())

    # Обрабатываем файл
    remove_first_k_chars_simple(input_filename, k_value, "result.txt")

    print(f"\nПосле удаления первых {k_value} символов:")
    with open("result.txt", 'r', encoding='utf-8') as f:
        print(f.read())
