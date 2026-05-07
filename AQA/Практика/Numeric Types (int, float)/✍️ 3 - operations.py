# Попросите пользователя ввести два числа и выведите их сумму, разность, произведение, частное, результат целочисленного деления и остаток от деления.

def operation(operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "//":
        return num1 // num2
    elif operation == "%":
        return num1 % num2
    else:
        return "Неверная операция"

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

print("Выберите операцию: +, -, *, /, //, %")
operation_input = input("Введите операцию: ")
result = operation(operation_input)
print(f"Результат: {result:g}")

