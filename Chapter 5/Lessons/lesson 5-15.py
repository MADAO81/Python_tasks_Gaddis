"""Мэрилин работает на "Интегрированные системы", компанию-разработчика программного 
обеспечения, которая имеет хорошую репутацию за превосходные дополнительные пособия 
своим сотрудникам. Одним из таких пособий является ежеквартальная премия, которая вы
 плачивается всем сотрудникам. Еще одним пособием является пенсионная программа для 
каждого сотрудника. Компания вносит 5% от заработной платы и премий каждого сотруд
 ника на их пенсионный счет. Мэрилин планирует написать программу, которая вычисляет 
взнос компании на пенсионный счет сотрудника за год. Она хочет, чтобы программа по 
отдельности показывала сумму взноса исходя из заработной платы и сумму взноса исходя из 
премий сотрудника. Вот алгоритм этой программы: 
Получить ежегодную заработную плату сотрудника до удержаний. 
Получить сумму выплаченных сотруднику премий. 
Рассчитать и показать взнос исходя из зарплаты. 
Рассчитать и показать взнос исходя из премий."""
# Use global constant
# Contribution rate of the company
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input("Enter salary: "))
    bonus = float(input("Enter the sum of bonuses: "))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

# Function show_pay_contrib accepts wages as an argument 
# and shows the contribution to pension savings based on this amount of payment.
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print("Contribution based on salary: $", format(contrib, ".2f"), sep = '')
    
# Function show_bonus_contrib accepts the amount of premiums 
# as an argument and shows the contribution to retirement savings based on this payment amount.
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print("Contribution based on the amount of premiums: $",format(contrib, ".2f"), sep = '' )
    
# Call main function 
main()
    
    
    
    