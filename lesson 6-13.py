# This program receives employee data from the user
# and saves it as records in the employees.txt file.

def main():
    # Get the number of employee records to create.
    num_emps = int(input("How many records of employee "
                         "do you want to create? "))

    # Open file to write
    emp_file = open("employees.txt", "w")

    # Get data for each employee and write it to a file.
    for count in range(1, num_emps +1):
        # Get data for employee
        print("Enter the data for employee № ", count, sep=" ")
        name = input("Name: ")
        id_num = input("ID: ")
        dept =  input("Department: ")

        # Write data to file as a record
        emp_file.write(name + "\n")
        emp_file.write(id_num + "\n")
        emp_file.write(dept + "\n")

        # Show empty line
        print()

    # Close the file
    emp_file.close()
    print("Employee records are saved to employees.txt")

# Call main function
main()

