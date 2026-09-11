#                                                                     Unique elements:
#                                                           Given a list with duplicates: [1, 2, 2, 3, 4, 4, 4, 5].
#                       Create a new list without duplicates. Combine the lists to produce two lists: the first containing no duplicates,
#                                                           and the second containing only the duplicates.


def unique_elements (numbers: list) -> tuple:
    unique = []
    duplicates = []

    for item in numbers:
        if item not in unique:
            unique.append(item)

        else:
            if item not in duplicates:
                duplicates.append(item)

    return unique, duplicates


numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique, duplicates = unique_elements(numbers)

print("Unique elements", unique)
print("Duplicates", duplicates)




















