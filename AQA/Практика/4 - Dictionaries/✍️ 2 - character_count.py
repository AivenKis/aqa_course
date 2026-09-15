#                                                                                       Character counting:
#                                                                                       The user enters a string.
#                                       Create a dictionary where the keys are the characters of the string and the values are their occurrence counts.


def count_characters(text:str) -> dict:
    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count


def print_character_count(char_count: dict):
    if not  char_count:
        print("ERROR: The string cannot be empty." )
        return

    print('\n Character count result:')
    print('-' * 50)

    for char, count in char_count.items():
        if char == " ":
            print(f"Пробел{' ':14}→ {count} раз")
        elif char == "\n":
            print(f"Новая строка{' ':8}→ {count} раз")
        else:
            print(f"'{char}'{' ':15}→ {count} раз")
    print("-" * 40)







