def get_name(prompt: str) -> str:
    while True:
        name = input(prompt).strip()

        if not name:
            print("ERROR: The first and last name cannot be empty.\n")
            continue

        if not  name.replace("-", "").replace("'", "").isalpha():
            print("ERROR: Name should contain only letters.\n")
            continue

        if len(name) < 2:
            print("ERROR: Name must be at least 2 characters long.\n")
            continue

        return name


def analyze_name(first_name: str, last_name:str) -> None:

    reversed_name = f"{last_name} {first_name}"
    upper_name = reversed_name.upper()
    total_length = len(first_name) + len(last_name) + 1

    print("\n" + "=" * 40)
    print(f"В обратном порядке:     {reversed_name}")
    print(f"Заглавными:             {upper_name}")
    print(f"Длина строки:           {total_length}")
    print("=" * 40)


first_name = get_name("Enter your first name: ")
last_name = get_name("Enter your last name: ")
analyze_name(first_name, last_name)






