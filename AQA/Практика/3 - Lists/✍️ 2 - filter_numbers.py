#                                                               Number filter:
#           Create a list of numbers from 1 to 20. Create a new list containing only the even numbers from the first list.


def filter_numbers(numbers):
    filtered_numbers = []

    for num in numbers:
        if num % 2 == 0:
            filtered_numbers.append(num)

    return filtered_numbers




numbers = list(range(1, 21))
even_numbers = filter_numbers(numbers)

print(f"Original list numbers:                {numbers}")
print(f"A list of even numbers only:          {even_numbers}")




