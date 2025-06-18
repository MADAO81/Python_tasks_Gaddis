#Budget analysis

monthly_budget = 0 # monthly Budget
expenses_name = [] # list of monthly expenses
expenses = 0 #the amount of monthly expenses
monthly_budget = float(input("Enter the amount of your monthly budget: "))
another_data = "y"
while another_data == "y" or another_data == "Y" or another_data == "yes" or another_data == "Yes":
    user_expenses_name = input("Enter the name of expense: ")
    expenses_name.append(user_expenses_name)
    expense = float(input("Enter the expence of amount: "))
    if expense >= 0:
        expenses +=expense
    else:
        print("You entered invalid data.The amount of expenses should be positive.")
        print("Please, enter the correct data.")
    another_data = input("Will you continue to calculate your expenses? y/n")
    
saved_money = monthly_budget - expenses #counting the saved money 
if saved_money > 0:
    print("Here's list of your expenses: ", expenses_name)
    print("Here's amount of your expenses: $", format(expenses, ",.2f"))
    print("You were able to save $",format(saved_money, ",.2f"), "this month.")
elif saved_money == 0:
    print("Here's list of your expenses: $", expenses_name)
    print("You haven't been able to save any money this month.")
elif saved_money < 0:
    print("Here's list of your expenses: ", expenses_name)
    print("You haven't been able to save any money this month.")
    print("Your overspending amounted to $",format(abs(saved_money), ".2f") )