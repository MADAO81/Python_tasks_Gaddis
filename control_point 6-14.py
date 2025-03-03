# There is a file data.txt that contains several lines of text.
# Write a short program using a while loop that displays
# all the lines in the file.

def main():
    lyrics = open("data.txt", "r")

    line = lyrics.readline()
    while line != "":
        print(line)
        line = lyrics.readline()
    lyrics.close()


main()
