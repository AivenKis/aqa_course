#                                                       Name Analyzer:
#                                           The user enters the first and last name.
#                   Print them in reverse order, capitalize all the letters, and calculate the total length of the string.


def get_name(prompt: str, min_length = 3) -> str:

    while True:
        name = input(prompt).strip()

        if not name:
            print("ERROR: The first and last name cannot be empty.\n")
            continue

        if not  name.replace("-", "").replace("'", ""). replace(" ", ""). isalpha():
            print("ERROR: Name should contain only letters.\n")
            continue

        if len(name) < min_length:
            print("ERROR: Name must be at least 2 characters long.\n")
            continue

        return name


def analyze_name(first_name: str, last_name:str) -> None:

    reversed_name = f"{last_name} {first_name}"
    upper_name = reversed_name.upper()
    total_length = len(first_name) + len(last_name) + 1

    print("\n" + "=" * 50)
    print(f"Reversed and Uppercase:             {upper_name}")
    print(f"Line length:                        {total_length}")
    print("=" * 50)


first_name = get_name("Enter your first name: ")
last_name = get_name("Enter your last name: ")
analyze_name(first_name, last_name)







