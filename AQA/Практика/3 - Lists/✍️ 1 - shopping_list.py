# Список покупок: Создайте список из 5 продуктов. Добавьте новый продукт, удалите второй элемент и отсортируйте список по алфавиту.

def shoping_list(list):
    products = ['Milk', 'Orange', 'Apple', 'Bread', 'Eggs']
    products.append('Meat')
    products.remove('Orange')
    products.sort()
    return products

print(shoping_list([]))