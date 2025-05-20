# 10-04

# import emp 
from objects import emp # the class is stored in the objects folder
def main():
    # Create three instances of the Employee class
    emp1 = emp.Employee("Antony Stark", "11111", "Management", "President")
    emp2 = emp.Employee("Bruce Wayne", "22222","Production", "Engineer")
    emp3 = emp.Employee("Peter Parker", "33333", "IT", "Intern")
    
    print("Employee 1: ")
    print(emp1)
    print()
    print("Employee 2: ")
    print(emp2)
    print()
    print("Employee 3: ")
    print(emp3)
    print()
    
# call main function 
main()