#The correspondence between degrees Celsius and degrees Fahrenheit
print("Celsius degree\tFahrenheit degree")
print("==================================")
for celsius_degree in range(0,21):
    fahrenheit_degree = 9 / 5 * celsius_degree + 32
    print(celsius_degree,format(fahrenheit_degree, ".2f"), sep ="\t\t")