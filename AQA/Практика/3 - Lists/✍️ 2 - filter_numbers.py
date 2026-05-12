def filter_numbers(numbers: list) -> list:
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

numbers = list(range(1, 21))
print(filter_numbers(numbers))




