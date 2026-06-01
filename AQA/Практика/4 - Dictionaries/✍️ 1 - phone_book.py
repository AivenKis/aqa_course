def add_contact(phone_book, name, phone):
    if name in phone_book:
        old_phone = phone_book[name]
        print(f"Контакт '{name}' уже существует. Номер телефона обновлен с {old_phone} на {phone}.")
    else:
        print(f"Контакт '{name}' добавлен с номером '{phone}'.")

    phone_book[name] = phone

    return phone_book



def delete_contact(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        print(f"Контакт '{name}' успешно удален.")
    else:
        print(f"Контакт '{name}' не найден.")

    return phone_book



def update_contact(phone_book, name, new_phone):

    if name in phone_book:
        old_phone = phone_book[name]
        phone_book[name] = new_phone
        print(f"Контакт '{name}' обновлен с номера '{old_phone}' на '{new_phone}'.")

    else:
        print(f"Контакт '{name}' не найден. Невозможно обновить номер телефона.")

    return phone_book



phone_book = {
    'Anton Shitov': 79664578899,
    "Ivan Elizarov": 79345672211,
    'Pavel Kulakov': 79432115677,
    'Helena Fisher': 79557779933
}




print("Тест 1: Добавление нового контакта")
phone_book = phone_book

result = add_contact(phone_book, 'Maria Petrova', 79876543210)

assert 'Maria Petrova' in result
assert result['Maria Petrova'] == 79876543210
print("OK")


print("\nТест 2: Удаление существующего контакта")
phone_book = phone_book
result = delete_contact(phone_book, 'Pavel Kulakov')

assert 'Pavel Kulakov' not in result
print("OK")


print("\nТест 3: Обновление существующего контакта")
phone_book = phone_book
result = update_contact(phone_book, 'Ivan Elizarov', 79999999999)

assert result['Ivan Elizarov'] == 79999999999
print("OK")
























