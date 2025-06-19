# Develop a program that generates seven-digit combination of lottery numbers.
# Program must generate seven random numbers from 0 to 9.
# After that write the loop shows contain of list.
import random


def main():
    lottery_numbers = [0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        lottery_numbers[i] = random.randint(0, 9)

    for i in range(7):
        print(lottery_numbers[i], end=" ")

        if i < 6:
            print(",", end="")


# main()

# def main():
#     lottery_numbers = []
#     while len(lottery_numbers) < 7:
#         lottery_numbers.append(random.randint(0, 9))
#
#     for i in lottery_numbers:
#         print(i, end=" ")
#
#
# main()
