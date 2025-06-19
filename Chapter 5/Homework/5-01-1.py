# converter miles to kilometres
def converter_kilometres_to_miles():
    kilometres = float(input("Enter the count of kilometres: "))
    miles = kilometres * 0.6214
    print(format(miles, ".2f"), "miles.")


converter_kilometres_to_miles()

# variant 2
# kilometres = float(input("Enter the count of kilometres: "))

# def converter_kilometres_to_miles(miles):
#     miles = kilometres * 0.6214
#     return miles

# print(format(converter_kilometres_to_miles(kilometres), ".2f"), "miles.")
