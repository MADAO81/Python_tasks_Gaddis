# task 10-07
# Personnel management system

# import emp 
from objects import emp 
import pickle 

# Global constants for menu items
LOOK_UP = 1 
ADD = 2 
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for the file name
# The file is located in the data subfolder
FILENAME = r"data\employees.dat" 

# Main function 
def main():
    # Get a dictionary of employees
    employees = load_employees()
    
    # Initialize a variable for user selection.
    choice = 0 
    
    # Process user requests until then the user exits the program.
    while choice != QUIT:
        choice = get_user_choice()
        
        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice == DELETE:
            delete(employees)
            
    # Pickle the resulting dictionary
    save_employees(employees)
    
def load_employees():
    try:
        # open file 
        input_file = open(FILENAME, "rb")
        
        # unpickle the dictionary
        employee_dict = pickle.load(input_file)
        
        # close file 
        input_file.close()
    except IOError:
        # Couldn't open the file.
        # Create an empty dictionary.
        employee_dict = {}
        
    return employee_dict
    
def get_user_choice
    # Show the menu, get the user's choice and check its validity.
	print()
	print("Menu")
	print("===================================")
    print("1. Find an employee")
    print("2. Add a new employee")
    print("3. Edit an existing employee")
    print("4. Delete an employee")
    print("5. Exit the program")
	print()
	
	choice = int(input("Enter your choice: "))
	
	# Check the selection.
	while choice < LOOK_UP or choice > QUIT:
	    choice = int(input("The choice you have made is unacceptable. Please enter a valid choice:"))
	    
	# Return user's choice
	return choice
	
def look_up(employees):
    # Get the employee identification number for the search.
    ID = input("Enter the employee's identification number: ")
    
    # Find the identifier in the dictionary. 
    # If found, the data will be printed using the employee __str__ method; 
    # otherwise, print the specified message.
    print(employees.get(ID, "The specified ID was not found"))
    
def add(employees):
    # Get information about an employee.
    name = input("Enter the employee's name: ")
    ID = input("Enter the employee ID: ")
    department = input("Enter the employee's department:  ")
    title = input("Enter the employee's title: ")
    
    new_emp = emp.Employee(name, ID, department, title)	
    
    # Add a new employee if the ID does not exist. Otherwise, notify the user that the ID exists.
    if ID not in employees:
        employees[ID] = new_emp 
        print("A new employee has been added.")
    else:
        print("An employee with this ID already exists.")
        
def change(employees):
    # Get updated information about the employee.
    ID = input("Enter the employee ID: ")
    
    # Change the information about the employee, if the ID exists. Otherwise, notify the user that the ID does not exist.
    if ID in employees:
        name = input("Enter the new name: ")
        department = input("Enter the new department: ")
        title = input("Enter the new title: ")
        
        new_emp = emp.Employee(name, ID, department, title)
        
        employees[ID] = new_emp
        print("The employee's information has been updated.")
    # ID not found
    else:
        print("The specified ID was not found.")
        
def delete(employees):
    # Get updated information about the employee.
    ID = input("Enter the employee ID: ")
    
    # Change the information about the employee, if the ID exists. Otherwise, notify the user that the ID does not exist.
    if ID in employees:
        del employees[ID]
        print("The employee's information has been deleted.")
    # ID not found
    else:
        print("The specified ID was not found.")
	
# The function pickles the specified dictionary and saves it in a file with employee data.
def save_employees(employees):
    # Open the file for record 
    output_file = open(FILENAME, "wb")
    
    # Pickle dictionary and save it 
    pickle.dump(employees, output_file)
    
    # close file 
    output_file.close()
    
# call main function
main()
	
	
	
	
	
	
	
    