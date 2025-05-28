Monthly_Income = int(input("Enter your monthly income: "))
Monthly_Expense = int(input("Enter your total monthly expenses: "))
Monthly_savings = Monthly_Income - Monthly_Expense
Projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)
print("Your monthly savings are: $", Monthly_savings)
print("Projected savings after one year, with interest, is: $", Projected_savings)
