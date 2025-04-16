# The most frequent symbol. Write a program that provides the user with 
# the ability to enter a string value and displays the character that appears
# in it most often.

# The function shows the character that appears most often in the string value. 
# If several characters have the same highest frequency, 
# then it shows the first character with that frequency.

def main():
    
    # Set local valuables
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = 0
    frequent = 0
    
    # Get user's input 
    user_string = input("Enter the string value: ")
    
    for ch in user_string:
        
        ch = ch.upper()
        
        # Determine index of letters
        index = letters.find(ch)
        if index >= 0:
            
            # Enlarge the array element corresponding to this letter.
            count[index] = count[index] + 1 
            
    for i in range(len(count)):
        if count[i] > count[frequent]:
            frequent = i 
            
    print("Most frequent symbol in string value: ", letters[frequent], ".", sep='')
    
# call main function
main()