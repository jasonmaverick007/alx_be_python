monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_Income - monthly_Expense
Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are: $", monthly_savings)
print("Projected savings after one year, with interest, is: $", Projected_savings)
