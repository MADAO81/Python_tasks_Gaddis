#This program uses a loop to output
#a table of numbers and their squares.

#Get the end limit
print("This program outputs a list of numbers")
print("and their squares.")
start_of_iterations = int(input("Enter the start of iterations: "))
end_of_iterations = int(input("Enter the end of iterations: "))

#Print the table headers
print()
print("Number\tSquare of the number")
print("============================")

#Print the numbers and their squares.
for number in range(start_of_iterations,end_of_iterations+1):
    square_of_the_number = number ** 2
    print(number,'\t', square_of_the_number)