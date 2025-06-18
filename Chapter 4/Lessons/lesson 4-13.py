#This program shows property taxes
tax_factor = 0.0065 #tax coefficient

#Get the number of the first lot
print("Enter the number of the property lot")
print("either 0 to end data processing.")
lot = int(input("Enter the lot number: "))

#Continue processing while the user
#will not enter 0.
while lot !=0:
    #Get the value of the property
    value = int(input("Enter the value of the property:"))
    
    #Calculate tax 
    tax = value * tax_factor
    
    #Show tax
    print("Property tax: $", format(tax,".2f"), sep = " ")
    
    #Get the next lot number
    print("Enter the number of the property lot")
    print("either 0 to end data processing.")
    lot = int(input("Enter the lot number: "))