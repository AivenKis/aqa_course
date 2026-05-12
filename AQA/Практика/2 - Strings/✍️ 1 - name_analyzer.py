def get_name_input (prompt: str) -> str:

    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print('The name cannot be empty. \n')
            continue

        if len(user_input) < 5 or len(user_input) > 25:
            print('The name must be between 5 and 25. \n')
            continue

        if not all(c.isalpha() or c.isspace() or c in "-'" for c in user_input):
            print('The name must contain only letters and spaces, hyphens (-) and apostrophesS. Special characters and numbers are not allowed.\n')
            continue

        return user_input

def name_analyzer():
    user_name = get_name_input('Enter your name and surname:')


    reversed_name = user_name[::-1]
    upper_name = reversed_name.upper()
    length = len(user_name)


    print("\n" + "=" * 40)
    print(f"В обратном порядке:   ,  {reversed_name}")
    print(f"Заглавными:           ,  {upper_name}")
    print(f"Длина строки:         ,  {length}")
    print("=" * 40)

name_analyzer()





















