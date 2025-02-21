# Mathematical test.
# Write a program that allows you to perform simple math tests.
# It should show two random numbers that should be summed like this:
#   555
# + 222
# This program should allow the learner to enter an answer. If the answer is correct,
# a congratulatory message should be displayed.
# If the answer is incorrect, a message with the correct answer should be displayed.

import random

NUM1 = random.randint(0, 1000)
NUM2 = random.randint(0, 1000)
print(" ", NUM1)
print("+", NUM2)

def math_quiz():
    sum_num = NUM1 + NUM2
    interrogation = int(input("Tell us the sum of these numbers: " ))
    if interrogation == sum_num:
        print("Correct!")
    else:
        print("Incorrect! Correct solution is: ", sum_num)

math_quiz()
