# Information about science courses.
def main():
    # create dictionary with audithoriums
    audithoriums = {"CS101":"3004", "CS102":"4501", "CS103":"6755", "CS104":"1244","CS105":"1411"}
    
    # create dictionary with teachers
    teachers = {"CS101":"Heinz", "CS102":"Alvarrado", "CS103":"Rich", "CS104":"Berque","CS105":"Lee"}
    
    # create dictionary with time of courses
    
    time ={"CS101":"8:00", "CS102":"9:00", "CS103":"10:00", "CS104":"11:00","CS105":"13:00"}
    
    course = input("Enter the number of the course: ")
    
    if course not in audithoriums:
        print("There is no such course!")
    else:
        print("Information about course ", course, ":")
        print("Audithorium: ",  audithoriums[course])
        print("Class start time: ", time[course])
        print("Teacher's name: ", teachers[course])
        
# call main function
main()