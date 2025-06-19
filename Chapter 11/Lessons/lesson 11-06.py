# that program creates Car, Truck, and SUV objects.

import vehicles 

def main():
    # Create a Car object for a used 2001 BMW car with 70,000 miles, priced at $15,000, with 4 doors.
    car = vehicles.Car("BMW", 2001, 70000, 15000.0, 4)
    
    # Create a Truck object for a used 2002 Toyota pickup truck with 40,000 mileage, price 
    # $12,000 and with 4-wheel drive.
    truck = vehicles.Truck("Toyota", 2002, 40000, 12000.0, "4WD")
    
    # Create an SUV object for a used 2000 A Volvo with 30,000 mileage, a price
    # tag of $18,500 and a capacity of 5 people.
    suv = vehicles.SUV("Volvo", 2000, 30000, 18500.0, 5)
    
    print("Used cars in stock.")
    print("====================")
    
    # Show passenger car data.
    print("This passenger car is available in stock: ")
    print("Manufacturer: ", car.get_make())
    print("Model: ", car.get_model())
    print("Mileage: ", car.get_mileage())
    print("Price: ", car.get_price())
    print("Doors: ", car.get_doors())
    print()
    
    # Show truck data.
    print("This truck is available in stock: ")
    print("Manufacturer: ", truck.get_make())
    print("Model: ", truck.get_make())
    print("Mileage: ", truck.get_mileage())
    print("Price: ", truck.get_price())
    print("Type of drive: ", truck.get_drive_type())
    print()
    
    # Show SUV data.
    print("This SUV is available in stock: ")
    print("Manufacturer: ", suv.get_make())
    print("Model: ", suv.get_model())
    print("Mileage: ", suv.get_mileage())
    print("Price: ", suv.get_price())
    print("Passenger capacity: ", suv.get_pass_cap())
    print()
    
# call main function
main()
    
    