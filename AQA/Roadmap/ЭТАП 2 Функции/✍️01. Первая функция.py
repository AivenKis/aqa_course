# 1 Данные (Тестовые наборы данных)

electronics = [
    {"name": "Mouse", "price": 50, "in_stock": True},
    {"name": "Laptop", "price": 1200, "in_stock": True},
    {"name": "Monitor", "price": 1500, "in_stock": False}
]

books = [
    {"name": "Python Book", "price": 300, "in_stock": True},
    {"name": "Old Magazine", "price": 500, "in_stock": False}
]

# 2. Объявление функции с передачей параметра
def get_max_price_in_stock(items):
    max_price = 0
    for items in electronics:
        if items["in_stock"] == True:
            if items["price"] > max_price:
                max_price = items["price"]

    for items in books:
        if items["in_stock"] == True:
            if items["price"] > max_price:
                max_price = items["price"]

    return max_price

# 3. Вызов функции с передачей аргумента и сохранение результата в переменную
max_elec = get_max_price_in_stock(electronics)
max_books = get_max_price_in_stock(books)


# 4. Проверка результата с помощью assert
print("Самая высокая цена в разделе 'Электроника': ", max_elec)
print("Самая высокая цена в разделе 'Книги': ", max_books)

assert max_elec == 1200
assert max_books == 300

print("All tests SUCCESS")
