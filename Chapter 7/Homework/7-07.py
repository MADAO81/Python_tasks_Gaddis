# Driving license test

def main():
    # Define variables
    solution = ['A', 'C', 'A', 'A', 'D',
                'B', 'C', 'A', 'C', 'B',
                'A', 'D', 'C', 'A', 'D',
                'C', 'B', 'B', 'D', 'A']
    correct_count = 0
    incorrect_count = 0
    incorrect_questions = []
    exam_pass = 15
    counter = 0

    try:
        # open file to read
        input_file = open(r"student_solution.txt", "r")
        # read all lines to list
        student_solutions = input_file.readlines()

        # Cut "\n" symbol from all elements of list
        for i in range(len(student_solutions)):
            student_solutions[i] = student_solutions[i].rstrip("\n")
        # Compare student's solution with key
        for i in range(len(student_solutions)):
            if student_solutions[i] == solution[i]:
                correct_count += 1
            else:
                incorrect_count += 1
                incorrect_questions.append(str(i + 1))

        # determine whether a student has passed an exam
        if correct_count >= exam_pass:
            print("Congratulations! Exam passed!")
        else:
            print("Sorry! Exam not passed. Try again.")

        print("Correct answers quantity: ", correct_count)
        print("Incorrect answers quantity: ", incorrect_count)

        if incorrect_count > 0:
            print("Questions you answered incorrectly: ")
            while counter < incorrect_count:
                print(incorrect_questions[counter])
                if counter + 1 < incorrect_count:
                    print(" , ")
                counter += 1

    except IOError:
        print('File not found')
    except IndexError:
        print('Indexing error')
    except:
        print('An error occured')


# call main function
main()
