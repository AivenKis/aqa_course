# Расчет бюджета: Создайте переменные для доходов и расходов. Посчитайте остаток, используя типы float.

def calculate_budget():
    budget_balance = income - expenses
    return budget_balance

income = float(input("Enter your income: "))
expenses = float(input("Enter your expenses: "))
budget_balance = income - expenses

print(f"Your budget balance is: {budget_balance:.2f}$")


