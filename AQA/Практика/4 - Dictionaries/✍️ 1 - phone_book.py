#                                                                                   Phonebook:
#                                           Create a dictionary where the keys are names and the values are phone numbers.
#                                                       Add a new entry, update an existing one, and delete one entry.

def add_contact(phone_book: dict, name: str, phone: str) -> dict:
    if name in phone_book:
        old = phone_book[name]
        print(f"Contact '{name}' already exists. Updated from {old} to {phone}.")
    else:
        print(f"Added new contact: '{name}' with number {phone}.")

    phone_book[name] = phone
    return phone_book



def update_contact(phone_book: dict, name: str, new_phone: str) -> dict:
    if name in phone_book:
        old = phone_book[name]
        phone_book[name] = new_phone
        print(f"Updated '{name}' from {old} to {new_phone}.")
    else:
        print(f"Contact '{name}' not found.")
    return phone_book



def delete_contact(phone_book: dict, name: str) -> dict:
    if name in phone_book:
        del phone_book[name]
        print(f"Contact '{name}' successfully deleted.")
    else:
        print(f"Contact '{name}' not found.")
    return phone_book


def print_phone_book(phone_book: dict, title: str):
    print(f"\n {title} ({len(phone_book)} contacts):")
    print("-" * 50)

    for name, phone in phone_book.items():
        print(f"{name:20} : {phone}")

    print("-" * 50)



phone_book = {
    'Anton Shitov':     '+7-966 457 88 99',
    'Ivan Elizarov':    '+7-934 567 22 11',
    'Pavel Kulakov':    '+7-943 211 56 77',
    'Helena Fisher':    '+7-957 779 93 53'
}

print_phone_book(phone_book, "Phone Book before changes")


print("\n=== TESTS ===")
add_contact(phone_book, 'Ivan Kiselev', '+7-987 654 32 10')
update_contact(phone_book, 'Ivan Elizarov', '+7-999 999 99 99')
delete_contact(phone_book, 'Pavel Kulakov')


print_phone_book(phone_book, "Phone Book after changes")




