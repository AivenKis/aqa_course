#                                           CHAPTER 4 User errors:
#                                           Everybody makes mistakes


def menu(choices, title = "Erik's Menu", prompt = "Choose your item"):
    print(title)
    print(len(title) * "-")

    i = 1  # - переменная как счётчик для нумерации пунктов меню
    for c in choices:
        print(i, c)
        i = i + 1
    while True:
        choice = input(prompt)  # - вывели значение аргумента prompt, получили ответ от пользователя

        allowed_answers = []

        for a in range(1, len(choice)+1):
            allowed_answers.append(str(a))
            allowed_answers.append('X')
            allowed_answers.append('x')

        if choice in allowed_answers:
            if choice == 'X' or choice == 'x':
                answer = ''
                break

            else:
                answer = choices[int(choice) - 1]  # - преобразовали значение в целое число берём элемент списка choices по нужному индексу
            break

        else:
            print("Invalid choice", "Enter number from 1 to", len(choices))
            answer = ''

    return answer #                 return — оператор возврата результата из функции.
#                                   После return функция заканчивает свою работу и возвращает значение.


#           Дальше идёт код вне функции — основная логика программы.
#           Здесь создаются списки (тип list) с вариантами:

drinks = ["hot chocolate", "coffee", "milkshake", "black tea", "green tea"]
flavors = ["caramel", "vanilla", "peppermint", "raspberry", "banana", "plain", "no additives"]
toppings = ["chocolate", "cinnamon", "caramel", "condensed milk", "no additives"]

#       Эти списки будут переданы в функцию menu в качестве параметра choices.
#       Функция вызывается, когда где-то в коде пишут её имя и круглые скобки с аргументами:

drink = menu(drinks, "Erik's drinks", "Choose your drink")
flavor = menu(flavors, "Erik's flavors", "Choose your flavor")
toppings = menu(toppings, "Erik's toppings", "Choose your topping")

print("Here is your order: ")
print("Main product: ", drink)
print("Flavor: ", flavor)
print("Topping: ", toppings)
print("Thanks for your order!")
