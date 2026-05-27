# Телефонная книга: Создайте словарь, где ключи — имена, а значения — номера телефонов.
# Добавьте новую запись, обновите существующую и удалите одну запись.

def unique(phonebook):
    unique = set()
    for phone in phonebook:
        if phone in unique:
            unique.remove(phone)





