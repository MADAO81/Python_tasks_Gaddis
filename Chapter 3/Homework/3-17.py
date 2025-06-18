print("WI FI does not work!")
answer = str(0)
print("Restart your computer and try to connect.")
print("Have you fixed the problem?")
answer = str(input())
if answer == "yes":
    print("Conrgatulations!")

if answer != "yes":
    print("Restart the router and try to connect.")
    print("Have you fixed the problem?")
    answer = str(input())
    if answer == "yes":
        print("Conrgatulations!")
        
if answer != "yes":
    print("Make sure that the cables between the router and the modem are firmly connected.")
    print("Have you fixed the problem?")
    answer = str(input())
    if answer == "yes":
        print("Conrgatulations!")
        
if answer != "yes":
    print("Move the router to a new location.")
    print("Have you fixed the problem?")
    answer = str(input())
    if answer == "yes":
        print("Conrgatulations!")
    else:
        print("Get a new router.")