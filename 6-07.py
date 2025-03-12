# There is a students. txt file on a disk. 
# It contains several records, and each record
# has two fields: the student's name and the student's grade for the final exam. 
# Write a program that deletes an entry with the student's name "John Pepper".

import os # this module needed for 'remove' and 'rename' functions

def main():
    # Create boolean value to use it as a flag
    found = False
    
    # Get the name of student, that you want to delete
    search = input("Which student do you want to delete?")
    
    # open original file
    my_file = open("students.txt", "r")
    
    # open temp file
    temp_file = open("temp.txt", "w")
    
    # read the field with description of first record
    descr = my_file.readline()
    
    # Read the rest of the file 
    while descr !="":
        # Read the field with grade
        grade = float(my_file.readline())
        
        # delete \n from description
        descr = descr.rstrip("\n")
        
        # If this record is not intented to deletion? record it to the temp file
        if descr != search:
            # write original record to the temp file
            temp_file.write(descr + "\n")
            temp_file.write(str(grade) + "\n")
        else:
            # set the "found" flag to True
            found = True
            
        # Read the next description
        descr = my_file.readline()
    
    # Close files
    my_file.close()
    temp_file.close()
    
    # Delete the original files
    os.remove("student.txt")
    
    # rename temp file
    os.rename("temp.txt", "students.txt")
    
    # If the value you are looking for is not found in the file, show message
    if found:
        print("File updated.")
    else:
        print("This value not found in file.")
        
# Call main functions
main()    