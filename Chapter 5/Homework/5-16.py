# Average grade and its level.
# Write a program that asks the user to enter five exam grades.
# The program should display the letter grade for each grade and the average grade.
# Write the following functions in the program:
# 'calc average' - the function should take five grades as arguments and return the average grade;
# 'determine grade' - the function must take a grade as an argument and return the letter grade
# level based on the given classification.
# Grade         Level
# 90 and higher   A
# 80-89           B
# 70-79           C
# 60-69           D
# Lower 60        F
def main():
    grade1 = int(input("Enter the first grade(0-100): "))
    grade2 = int(input("Enter the second grade(0-100): "))
    grade3 = int(input("Enter the third grade(0-100): "))
    grade4 = int(input("Enter the fourth grade(0-100): "))
    grade5 = int(input("Enter the fifth grade(0-100): "))
    # if grade1 >= 0 and grade1 <= 100:
    #     grade2 = int(input("Enter the second grade(0-100): "))
    #     if grade2 >= 0 and grade2 <= 100:
    #         grade3 = int(input("Enter the third grade(0-100): "))
    #         if grade3 >= 0 and grade3 <= 100:
    #             grade4 = int(input("Enter the fourth grade(0-100): "))
    #             if grade4 >= 0 and grade4 <= 100:
    #                 grade5 = int(input("Enter the fifth grade(0-100): "))
    #                 if grade5 <= 0 and grade5 >= 100:
    #                     print("Error! Entered value is incorrect."
    #                           "The grade must be between 0 and 100.")
    #             else:
    #                 print("Error! Entered value is incorrect."
    #                       "The grade must be between 0 and 100.")
    #         else:
    #             print("Error! Entered value is incorrect."
    #                   "The grade must be between 0 and 100.")
    #     else:
    #         print("Error! Entered value is incorrect."
    #               "The grade must be between 0 and 100.")
    # else:
    #     print("Error! Entered value is incorrect."
    #           "The grade must be between 0 and 100.")

    average_grade = calc_average(grade1, grade2, grade3, grade4, grade5)
    stud_level = determine_grade(calc_average(grade1, grade2, grade3, grade4, grade5))
    print(f"Your average grade: {average_grade}")
    print(f"Your level is: {stud_level}")


def calc_average(*args):
    total_score = 0
    counter = 0
    for el in args:
        total_score += el
        counter += 1
    average = total_score / counter
    return average


def determine_grade(average):
    level = 0
    if average >= 90:
        level = "A"
    elif 80 <= average < 90:
        level = "B"
    elif 70 <= average < 80:
        level = "C"
    elif 60 <= average < 70:
        level = "D"
    else:
        level = "E"

    return level


main()
