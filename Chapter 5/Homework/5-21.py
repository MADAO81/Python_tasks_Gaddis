# A random number guessing game.
# Write a program that generates a random  number in the range from 1 to 100 
# and asks the user to guess this number. If the user's guess is greater than 
# a random number, the program should display the message "Too big, try again." 
# If the guess is less than a random number, the program should display 
# the message "Too little, try again". If the user guesses the number, 
# the application should congratulate the user and generate a new random 
# number to resume the game.
# Optional improvement: Improve the game so that it counts the guesses that
# the user makes. When the user guesses a random number correctly, the program should show the number of guesses.
import random   
counter = 0
number = random.randint(1,100)
print("Let's play a game. What number did I have in mind?")
print(number)
user_number = int(input("Enter the number: "))
while user_number != number:
    counter += 1 
    if user_number < number:
        print("Too little, try again")
        user_number = int(input("Enter the number: "))
    elif user_number > number:
        print("Too much, try again")
        user_number = int(input("Enter the number: "))

print("You win!")
print(f"You have made {counter} attempts. ")