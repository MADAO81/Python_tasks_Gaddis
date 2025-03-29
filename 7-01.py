# Sales amount. Develop a program that asks the user to enter sales for each day of the week.
# The amounts must be saved in the list. Use a loop to calculate the total sales and display the result.

def main():
    sales = []  # Create an empty list
    sales_amount = 0.0 # Create an empty sum
    while len(sales) != 7:
        day_revenue = input("Enter daily revenue: ")
        sales.append(float(day_revenue))
    print(f"The revenue for each day was ${sales}")
    for daily_revenue in sales:
        sales_amount += daily_revenue
    print(f"Total sales: {sales_amount:,.2f} $")

# Call main function
main()

# def main():
#     # Переменные
#     total_sales = 0.0
#
#     # Инициализировать списки
#     daily_sales = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#     days_of_week = ['понедельник', 'вторник', 'среда',
#                     'четверг', 'пятница', 'суббота',
#                     'воскресенье']
#
#     for i in range(7):
#         daily_sales[i] = float(input('Введите продажи за ' \
#                                      + days_of_week[i] + ': '))
#
#     for number in daily_sales:
#         total_sales += number
#
#     # Показать общий объем продаж
#     print ('Общий объем продаж за неделю: $', \
#            format(total_sales, ',.2f'), sep='')
#
# # Вызвать главную функцию.
# main()