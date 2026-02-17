#                                           CHAPTER 3
#                                     Functions: Don’t repeat yourself!

def menu(choices, title="Erik's Menu", prompt="Choose your item: "):
    print(title)
    print(
        len(title) * "-")  # берем аргумент title, вычисляем его длину и выводим строку из тире точно такого же размера

    i = 1  # - переменная как счётчик для нумерации пунктов меню
    for c in choices:
        print(i, c)
        i = i + 1

    choice = input(prompt)  # - вывели значение аргумента prompt, получили ответ от пользователя
    answer = choices[int(choice) - 1]

    return answer


#           Дальше идёт код вне функции — основная логика программы.
#               Здесь создаются списки (тип list) с вариантами:

drinks = ["hot chocolate", "coffee", "milkshake", "black tea", "green tea"]
flavors = ["caramel", "vanilla", "peppermint", "raspberry", "banana", "plain"]
toppings = ["chocolate", "cinnamon", "caramel", "condensed milk"]

#       Эти списки будут переданы в функцию menu в качестве параметра choices.

drink = menu(drinks, "Erik's drinks", "Choose your drink")
flavor = menu(flavors, "Erik's flavors", "Choose your flavor")
toppings = menu(toppings, "Erik's toppings", "Choose your toppings")

print("Here is your order: ")
print("Main product: ", drink)
print("Flavor: ", flavor)
print("Topping: ", topping)
print("Thanks for your order!")
