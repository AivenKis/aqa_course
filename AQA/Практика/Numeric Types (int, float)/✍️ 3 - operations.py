def validate_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))

        except ValueError:
            print("ERROR! Please enter a number.\n")


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


num1 = validate_input ("Введите первое число: ")
num2 = validate_input ("Введите второе число: ")


print("\nВыберите операцию: +, -, *, /, //, %")
operation_input = input("Введите операцию: ")

result = operation(operation_input)

print(f"Результат: {result:g}")

