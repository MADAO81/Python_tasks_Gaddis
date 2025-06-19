ch = "1, 2, 3 o'clock, 4 o'clock, rock,"
print("Here your line: ",ch)
if any(character.isdigit() for character in ch):
    print("There are numbers in the line.")
else:
    print("There are not numbers in the line.")
    