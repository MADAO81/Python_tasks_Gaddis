#Endless cycle
keep_going = "yes"
while keep_going == "yes":
    sales = float(input("Enter the total sales: "))
    commission_rate = float(input("Enter the commission rate: "))
    commission = sales * commission_rate
    print("Commission rate is : $", format(commission,".2f"), sep =' ')
