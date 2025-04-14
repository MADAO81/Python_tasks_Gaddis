# write a function that takes a string value as an argument and calls the string value in reverse order.

user_string = input("Enter your message: ")

def user_string_reverse(somestring):
    new_string = ""
    for ch in range(len(somestring)-1,-1,-1):
        new_string += somestring[ch]
    return new_string
    
print("Here is your reverse message:", user_string_reverse(user_string))