# Revise the program you wrote above, using a 'for' loop instead of a 'while' loop.

def main():
    lyrics = open("data.txt", "r")

    line = lyrics.readline()
    for line in lyrics:
        print(line)
    lyrics.close()


main()
