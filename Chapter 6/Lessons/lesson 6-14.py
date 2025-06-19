# This program shows the records that are in the file employees.txt

def main():
    # Open file employees.txt
    emp_file = open("employees.txt", "r")

    # Read the first line in the file
    name = emp_file.readline()

    # If the field is read, then continue processing
    while name != "":
        # Read the field wit ID
        id_num = emp_file.readline()

        # Read the field with Department
        dept = emp_file.readline()

        # Remove newline characters from fields.
        name = name.rstrip("\n")
        id_num = id_num.rstrip("\n")
        dept = dept.rstrip("\n")

        # Show the record
        print("Name: ", name)
        print("ID: ", id_num)
        print("Department: ", dept)
        print()

        # Read the field with the name of the next record.
        name = emp_file.readline()

    # Close the file
    emp_file.close()

# Call main function
main()
