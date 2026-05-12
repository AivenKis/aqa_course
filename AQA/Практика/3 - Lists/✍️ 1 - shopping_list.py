def shopping_list(products: list) -> list :
    if len(products) > 1:
        products.pop(1)

    products.append('Meat')
    products.sort()

    return products

products = ['Milk', 'Orange', 'Apple', 'Bread', 'Eggs']
result = shopping_list(products)
print(result)
