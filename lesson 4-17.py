num_students = int(input("How many students?"))
num_test_scores = int(input("How many grades does each student have?"))
for student in range(num_students):
    total = 0.0 #Initialize the rating accumulator.
    print("Student number", student + 1)
    print("================")
    for test_num in range(num_test_scores):
        print("Lab work number", test_num + 1, end = " ")
        score = float(input(": "))
        total +=score
    #Calculate the average score of this student.
    average = total / num_test_scores
    
    #Show the average score.
    print("The average score of student number",student + 1, "is: ", format(average, ".2f"))
    print()