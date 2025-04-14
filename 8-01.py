# Initials. Write a program that receives a string value containing 
# the name, patronymic and surname of the person and shows the initials. For example, if the user
# enters Mikhail Ivanovich Kuznetsov, the program should output a MIK.


def main():
    name = input("Enter the first name, patronimic and last name: ")
    name = name.upper().split(" ")
    for string in name:
        print(string[0],".", sep = "", end = "")
    

main()
