# This program demonstrates the Car class

import vehicles

def main():
    # Create an object based on the Car class. 
    # Passenger car: 2007 Audi with 12,500 miles,
    # priced at $21500.00 and with 4 doors.
    used_car = vehicles.Car("Audi", 2007, 12500, 21500.0, 4)
    
    # Show info about car 
    print("Manufacturer: ", used_car.get_make())
    print("Model: ", used_car.get_model())
    print("Mileage: ", used_car.get_mileage())
    print("Price: ", used_car.get_price())
    print("Doors quantity: ", used_car.get_doors())
    
# call main function
main()
