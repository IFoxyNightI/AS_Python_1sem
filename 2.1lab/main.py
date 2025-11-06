if __name__ == "__main__":
    pass
def merge(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result
def sort_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))
def clear_lists(d):
    return  {k: [] if type(v) == list else v for k, v in d.items()}
print("Введите словари:")
dicts = []
i = 1
while True:
    user_input = input(f"Словарь {i} (Enter для завершения ввода): ")
    if user_input == "":
        break
    try:
        d = eval(user_input)
        if type(d) == dict:
            dicts.append(d)
            print(f"Был добавлен словарь {i}")
            i += 1
        else:
            print("Это не словарь")
    except:
        print("Ошибка, пример формата: {1:2, 'a':'b'}")
merged = merge(*dicts)
print(f"Объединение: {merged}")
sorted = sort_values(merged)
print(f"Сортировка: {sorted}")
cleared = clear_lists(merged)
print(f"Очистка: {cleared}")
