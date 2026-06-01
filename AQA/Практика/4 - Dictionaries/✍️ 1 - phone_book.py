# Телефонная книга: Создайте словарь, где ключи — имена, а значения — номера телефонов.
# Добавьте новую запись, обновите существующую и удалите одну запись.
# Если имя уже есть в словаре — обновляла номер телефона.
# Если имени нет — добавляла новую запись.

phone_book = {
    'Anton Shitov': 79664578899,
    "Ivan Elizarov": 79345672211,
    'Pavel Kulakov': 79432115677,
    'Helena Fisher': 79557779933
}



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



























