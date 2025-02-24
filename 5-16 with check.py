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
    grade1 = check_number(input)
    grade2 = check_number(input)
    grade3 = check_number(input)
    grade4 = check_number(input)
    grade5 = check_number(input)

    average_grade = calc_average(grade1, grade2, grade3, grade4, grade5)
    stud_level = determine_grade(calc_average(grade1, grade2, grade3, grade4, grade5))
    print(f"Your average grade: {average_grade}")
    print(f"Your level is: {stud_level}")
    

def check_number(num):
    while True:
        try:
            num = int(input("Enter the grade 1-100: "))
        except ValueError:
            print("Please enter a valid grade 1-100")
            continue
        if num >= 1 and num <= 100:
            return num
            break
        else:
            print('The grade must be in the range 1-100')
            
            
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