max_temp = 102.5
temperature = float(input("Enter the temperature of the substance in Celsius degrees:"))

while temperature > max_temp:
    print("The temperature is too high")
    print("Reduce the heat and wait")
    print("5 minutes. Then check the temperature")
    print("again and enter the received value.")
    temperature = float(input("Enter a new temperature value: "))

print("The temperature is OK.")
print("Check it again in 15 minutes.")
    