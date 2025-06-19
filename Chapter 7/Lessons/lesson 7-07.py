# This program calculates salary for every employee

# NUM_EMPLOYEES used as global constant for size of list

NUM_EMPLOYEES = 6

def main():
    # Create list with work hours
    hours = [0] * NUM_EMPLOYEES
    
    # Get work hours for every employee
    for index in range(NUM_EMPLOYEES):
        print("Enter the number of hours worked by the employee: ", 
        index + 1, ":", sep = " ", end = " ")
        hours[index] = float(input())
        
    # Get an hourly pay rate
    pay_rate = float(input("Enter the hourly pay rate: "))
    
    # Show wage for every employee
    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print(f"Employee's salary {index +1 }: $ {gross_pay:.2f}")
        
# call main function
main()