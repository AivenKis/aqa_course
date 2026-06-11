def get_first_name():
    while True:
        first_name = input("Enter your first name: ")

        if not first_name:
            print("ERROR: The first and last name cannot be empty.\n")
            continue

        if len(first_name) < 3:
            print("ERROR: Please enter both first name and last name (at least 3 symbols).\n")
            continue

        return first_name



def get_last_name():
    while True:
        last_name = input("Enter your last name: ")

        if not last_name:
            print("ERROR: The last name cannot be empty.\n")
            continue

        if len(last_name) < 3:
            print("ERROR: Please enter both last name (at least 3 symbols).\n")
            continue

        return last_name


def analyze_name(first_name, last_name):

    reversed_name = f"{last_name} {first_name}"
    upper_name = reversed_name.upper()
    total_length = len(first_name) + len(last_name) +1

    print("\n" + "=" * 40)
    print(f"В обратном порядке:     {reversed_name}")
    print(f"Заглавными:             {upper_name}")
    print(f"Длина строки:           {total_length}")
    print(f"Длина строки:           {total_length}")
    print("=" * 40)


first_name = get_first_name()
last_name = get_last_name()
analyze_name(first_name, last_name)






