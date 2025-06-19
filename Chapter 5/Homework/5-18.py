# Prime numbers.
# Write the Boolean function is _prime, which takes an integer as an argument
# and returns true if the argument is a prime number, or false otherwise. 
# Apply a function in the program that prompts the user to enter a number 
# and then displays a message indicating whether this number is prime.
number = int(input("Enter the number: "))


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False 
    return True 


check = is_prime(number)

if check == True:
    print(f"Number {number} is prime!")
else:
    print(f"Number {number} is not prime!")
