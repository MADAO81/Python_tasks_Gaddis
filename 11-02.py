# task 11-02

# ShiftSupervisor class 
from objects import emp_full 

def main():
    # Local valuables
    super_name = ""
    super_id = ""
    super_salary = 0.0 
    super_bonus = 0.0 
    
    # Get data attributes 
    super_name = input("Enter name: ")
    super_id = input("Enter ID: ")
    super_salary = float(input("Enter the annual salary: "))
    super_bonus = float(input("Enter the bonus payment: "))
    
    # Create an instance of the ShiftSupervisor class.
    supervisor = emp_full.ShiftSupervisor(super_name, super_id, super_salary, super_bonus)
    
    # Show information 
    print("Information about the shift supervisor: ")
    print("Name: ", supervisor.get_name())
    print("ID: ", supervisor.get_id_number())
    print("Annual salary: ", supervisor.get_salary(), ",.2f". sep = "")
    print("Annual bonus: $", format(supervisor.get_bonus(), ",.2f"), sep = "")
    
# call main function 
main()
    