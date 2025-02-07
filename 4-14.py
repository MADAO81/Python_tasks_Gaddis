quantity_symbols = int(input("Enter the start quantity of symbols: "))
for i in range(quantity_symbols,0,-1):
    for g in range(i):
        print("*", end = " ")
    print()
    