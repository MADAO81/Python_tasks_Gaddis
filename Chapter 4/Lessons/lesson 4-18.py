rows = int(input("How many rows?"))
col = int(input("How many columns?"))

for r in range(rows):
    for c in range(col):
        print("*", end = " ")
    print()