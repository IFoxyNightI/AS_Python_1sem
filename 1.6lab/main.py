if __name__ == "__main__":
    pass
text = input("Введите строку: ")
first_char = text[0]
result = first_char + text[1:].replace(first_char, '$')
print(f"Результат: {result}")
