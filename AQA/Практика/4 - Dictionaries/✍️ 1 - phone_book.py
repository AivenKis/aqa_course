
def add_contact(phone_book, name, phone):
    if name in phone_book:
        old_phone = phone_book[name]
        print(f"Контакт '{name}' уже существует. Номер телефона обновлен с {old_phone} на {phone}.")
    else:
        print(f"Контакт '{name}' добавлен с номером '{phone}'.")

    phone_book[name] = phone

    return phone_book



def update_contact(phone_book, name, new_phone):

    if name in phone_book:
        old_phone = phone_book[name]
        phone_book[name] = new_phone
        print(f"Контакт '{name}' обновлен с номера '{old_phone}' на '{new_phone}'.")
    else:
        print(f"Контакт '{name}' не найден. Невозможно обновить номер телефона.")

    return phone_book




def delete_contact(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        print(f"Контакт '{name}' успешно удален.")
    else:
        print(f"Контакт '{name}' не найден.")

    return phone_book


# ========================== ТЕСТИРОВАНИЕ ================================================

phone_book = {
    'Anton Shitov': 79664578899,
    "Ivan Elizarov": 79345672211,
    'Pavel Kulakov': 79432115677,
    'Helena Fisher': 79557779933
}


print("\nТелефонная книга до изменений содержит", len(phone_book), "записи:", phone_book)

print("\nТест 1: Добавление нового контакта")
result = add_contact(phone_book, 'Ivan Kiselev', 79876543210)

assert 'Ivan Kiselev' in result
assert result['Ivan Kiselev'] == 79876543210
print("PASSED")


print("\nТест 2: Обновление существующего контакта")
result = update_contact(phone_book, 'Ivan Elizarov', 79999999999)

assert result['Ivan Elizarov'] == 79999999999
print("PASSED")



print("\nТест 3: Удаление существующего контакта")
result = delete_contact(phone_book, 'Pavel Kulakov')

assert 'Pavel Kulakov' not in result
print("PASSED\n")

print("\nТелефонная книга после изменений содержит", len(phone_book), "записи:", phone_book)




























