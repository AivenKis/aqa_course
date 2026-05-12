def unique_elements(lst: list) -> tuple:
    unique = []
    duplicates = []

    for item in lst:
        if item not in unique:
            unique.append(item)
        else:
            if item not in duplicates:
                duplicates.append(item)
    return unique, duplicates


def filter_numbers(lst: list) -> tuple:
    unique, duplicates = unique_elements(lst)
    return unique, duplicates

numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique, duplicates = filter_numbers(numbers)


print("Уникальные элементы:", unique)
print("Дубликаты:", duplicates)


