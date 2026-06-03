def count_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def print_character_count(char_count):
    print(char_count)
    print()

    for char, count in char_count.items():
        if count == 1:
            print(f"Символ '{char}' встречается {count} раз" )
        elif count in (2, 3, 4):
            print(f"Символ '{char}' встречается {count} раза")
        else:
            print(f"Символ '{char}' встречается {count} раз")

def main():
    user_input = input('Введите пожалуйста строку для анализа: ')
    result = count_characters(user_input)
    print_character_count(result)


if __name__ == '__main__':
    main()

