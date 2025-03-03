# Write a short program that uses a 'for' loop to write numbers from 1 to 10 to a file.
def main():
    numberfile = open("controlnumbers.txt", "w")
    for number in range(1,11):
        numberfile.write(str(number) + "\n")
        print(number)

    numberfile.close()

main()
