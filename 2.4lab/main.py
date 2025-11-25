if __name__ == "__main__":
    pass
#a
def split_string(text, delimiter=" "):
    return text.split(delimiter)
#Пример:
print(split_string("яблоко виноград дыня"))
print(split_string("one,two,three", delimiter=","))

#б
def compare_elements(list1, list2, comparison_function=None):
    if comparison_function is None:
        comparison_function = lambda x, y: x == y
    result = []
    min_length = min(len(list1), len(list2))
    for i in range(min_length):
        if comparison_function(list1[i], list2[i]):
            result.append((list1[i], list2[i]))
    return result
#Пример:
print(compare_elements([1, 2, 3], [1, 4, 3]))
print(compare_elements([1, 2, 3], [4, 5, 6], comparison_function=lambda x, y: x + y > 5))

#в
def count_unique_chars(*strings):
    all_chars = ""
    for string in strings:
        all_chars += string

    return len(set(all_chars))
#Пример:
print(count_unique_chars("hello", "world"))
print(count_unique_chars("abc", "def", "ghi"))

#г
def common_elements(*lists):
    if not lists:
        return []
    common_set = set(lists[0])
    for lst in lists[1:]:
        common_set = common_set.intersection(set(lst))
    return list(common_set)
#Пример:    
print(common_elements([1, 2, 3], [2, 3, 4], [3, 4, 5]))
print(common_elements(["a", "b"], ["b", "c"], ["b", "d"]))
