
def calculate_budget():

    while True:
        try:
            income = float(input("Enter your income: "))
            expense = float(input("Enter your expense: "))
            if income < 0 or expense < 0:
                print("Income and expense should be non-negative. Please try again.\n")
                continue
            return income, expense
        except ValueError:
            print("Income and expense should be non-negative. Please try again.\n")

income, expense = calculate_budget()
budget = income - expense

print(f"Your budget is {budget:.2f}$.")






