# Car class 

# import car 
from objects import car:
    
def main():
    # Create an instance of the Car class.
    my_car = car.Car("2021", "Toyota Land Cruiser Prado")
    
    # Accelerate 5 times 
    print( "Car accelerates: ")
    for i in range(5):
        my_car.accelerate()
        print("Current speed: ", my_car.get_speed())
    print()
    
    # Slow down 5 times 
    print("Car is slow down: ")
    for i in range(5):
        my_car.brake()
        print("Current speed: ", my_car.get_speed())
        
# Call main function
main()