# converter miles to kilometres
kilometres = float(input("Enter the count of kilometres: "))

def converter_kilometres_to_miles(miles):
    miles = kilometres * 0.6214
    return miles
    
print(format(converter_kilometres_to_miles(kilometres), ".2f"), "miles.")