#                                                                   Shopping list:
#                       Create a list of 5 products. Add a new product, delete the second item, and sort the list alphabetically.

def shopping_list(products: list) -> list:
    products.append("Meat")
    del products[1]
    products.sort()



products = ["Milk", "Orange", "Cheese", "Apple", "Banana"]
shopping_list(products)
print(products)






