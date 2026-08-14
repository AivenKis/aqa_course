#                                                               Budget calculation:
#                                           Create variables for income and expenses. Calculate the remainder using float types.


def get_income():

    while True:
        try:
            value = float(input("Please enter a income: "))
            if value < 0:
                print("Income should be non-negative. Please try again.\n")
                continue
            return value
        except ValueError:
            print("ERROR: Please enter a numeric value.\n")

def get_expense():
    while True:
        try:
            value = float(input("Please enter a expense: "))
            if value < 0:
                print("Expense should be non-negative. Please try again.\n")
                continue
            return value
        except ValueError:
            print("ERROR: Please enter a numeric value.\n")

def calculate_budget(income, expense):
    return income - expense


income = get_income()
expense = get_expense()
budget = calculate_budget(income, expense)
print(f"Your budget is: {budget:.2f}$")



