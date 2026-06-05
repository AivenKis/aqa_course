def input_number(prompt: str):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a numeric value.\n")

def display_results(num1: float, num2: float):
    print()
    print(f"Operations result: ")
    print('_______________________')
    print(f"Sum:                                {num1 + num2:g}")
    print(f"Difference:                         {num1 - num2:g}")
    print(f"Multiplication:                     {num1 * num2:g}")

    if num2 != 0:
        print(f"Quotient:                           {num1 / num2:g}")
        print(f"Integer Division:                   {num1 // num2:g}")
        print(f"Remainder:                          {num1 % num2:g}")
    else:
        print("Cannot divide by zero.")

num1 = input_number("Enter first number: ")
num2 = input_number("Enter second number: ")

display_results(num1, num2)


