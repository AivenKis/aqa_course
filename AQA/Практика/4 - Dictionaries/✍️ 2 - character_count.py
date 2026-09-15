#                                                                                       Character counting:
#                                                                                       The user enters a string.
#                                       Create a dictionary where the keys are the characters of the string and the values are their occurrence counts.


def count_characters(text:str) -> dict:
    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count


def print_results(char_count: dict):
    print('\nCharacter count result:')
    print('-' * 50)


    for char, count in char_count.items():
        if char == " ":
            print(f"Space{' ':14} → {count} times")
        else:
            print(f"'{char}'{' ':16} → {count} times")
    print("-" * 50)



while True:
    user_input = input('Please enter a string for analysis: ').strip()



    if not user_input:
        print("ERROR: The string cannot be empty.\n" )
        continue

    lower_text = user_input.lower()
    result = count_characters(lower_text)
    print_results(result)
    break



