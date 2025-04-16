# Vowels and consonants. Write a program with a function that
# takes a string value as an argument and returns the number of vowels it contains. 
# The application must have another function that takes as an argument 
# a string value and returns the number of consonants it contains. The application should provide 
# the user with the opportunity to enter a string value and display the number of vowels and consonants contained in it.

def main():
    # local valuables
    vowels = 0
    consonants = 0
    
    # get string value from user
    user_string = input("Enter the string value: ")
    
    # Call vowel_counter function and save result
    vowels = vowel_counter(user_string)
    
    # Call consonant_counter and save result
    consonants = consonant_counter(user_string)
    
    # Show result
    print("Entered string value contains: ", vowels, "vowels", consonants, "consonants")
    
# vowel_counter function gets string value and returns quantity of vowels in string.
def vowel_counter(string):
    # local valuables
    count = 0
    vowels = 'аеёиоуыэюяaeuiyo'
    
    # determine vowels
    for ch in string:
        if vowels.find(ch) >=0:
            count +=1
            
    # return vowels quantity
    return count
    
# consonant_counter function gets string value and returns quantity of consonants in string.
def consonant_counter(string):
    # local valuables
    count = 0 
    consonants = 'бвгджзйклмнпрстфхцчшщъьqwrtpsdfghjklzxcvbnm'
    
    # determine consonants
    for ch in string:
        if consonants.find(ch) >= 0:
            count += 1
            
    # returns consonants quantity
    return count
    
# call main function
main()
    
  
   
    
    
    
    
    
    
    